"""Servidor web local do CaosZero.

Expõe a interface gráfica (pasta ``ui/``) e uma API JSON mínima para
organizar, desfazer e diagnosticar pastas. Pensado para uso local: não tem
autenticação e não deve ser exposto à internet.
"""

from __future__ import annotations

import json
import logging
import os
import sys
import threading
import webbrowser
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from .config import Config, load_config
from .demo import criar_sandbox
from .errors import CaosZeroError
from .executor import execute_plan, undo_run
from .journal import Journal
from .logging_setup import configure_logging
from .planner import PlanOptions, build_plan
from .system_info import collect_system_info
from .utils import parse_size

LOGGER = logging.getLogger("caoszero.web")


def _repo_root() -> Path:
    # Quando congelado (PyInstaller), os recursos ficam em sys._MEIPASS.
    if getattr(sys, "frozen", False):
        return Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parents[2]))
    return Path(__file__).resolve().parents[2]


def _ui_dir() -> Path:
    return _repo_root() / "ui"


def _default_target(value) -> Path:
    raw = value or os.environ.get("CAOSZERO_TARGET") or "."
    return Path(str(raw)).expanduser()


def _options_from(data: dict) -> PlanOptions:
    def _int(key):
        v = data.get(key)
        if v is None or v == "":
            return None
        return int(v)

    min_size = data.get("min_size")
    if isinstance(min_size, str) and min_size:
        min_size = parse_size(min_size)
    max_size = data.get("max_size")
    if isinstance(max_size, str) and max_size:
        max_size = parse_size(max_size)

    return PlanOptions(
        recursive=bool(data.get("recursive", False)),
        include_hidden=bool(data.get("hidden", False)),
        pattern=data.get("pattern") or None,
        older_than=_int("older_than"),
        archive_old_days=_int("archive_old"),
        rename_pattern=data.get("rename") or None,
        rename_only=bool(data.get("rename_only", False)),
        category=data.get("category") or None,
        min_size=min_size,
        max_size=max_size,
    )


def _plan_to_dict(plan) -> dict:
    return {
        "target": str(plan.target),
        "scanned": plan.scanned,
        "counts": plan.counts(),
        "operations": [
            {
                "action": op.action.value,
                "source": str(op.source),
                "source_name": op.source.name,
                "destination": str(op.destination) if op.destination else None,
                "destination_name": op.destination.name if op.destination else None,
                "category": (op.destination.parent.name if op.destination else "—"),
                "reason": op.reason,
                "size": op.size,
                "status": op.status.value,
            }
            for op in plan.operations
        ],
        "skipped": [{"path": str(s.path), "reason": s.reason} for s in plan.skipped],
        "warnings": list(plan.warnings),
    }


class CaosZeroHandler(SimpleHTTPRequestHandler):
    """Handler que serve a UI e a API JSON."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(_ui_dir()), **kwargs)

    # --- helpers ---------------------------------------------------------
    def _send_json(self, payload, status=HTTPStatus.OK):
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _read_json(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length) if length else b""
        if not raw:
            return {}
        return json.loads(raw.decode("utf-8"))

    def _error(self, message, status=HTTPStatus.BAD_REQUEST):
        self._send_json({"error": message}, status=status)

    # --- routing ---------------------------------------------------------
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path == "/" or path == "":
            # redireciona para a galeria
            self.send_response(HTTPStatus.FOUND)
            self.send_header("Location", "/index.html")
            self.end_headers()
            return
        if path == "/api/doctor":
            params = parse_qs(parsed.query)
            target = _default_target(params.get("target", [None])[0])
            try:
                info = collect_system_info(target)
                self._send_json({"target": str(target), "info": info})
            except Exception as exc:  # noqa: BLE001
                self._error(str(exc), status=HTTPStatus.INTERNAL_SERVER_ERROR)
            return
        # arquivos estáticos (ui/)
        super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        try:
            data = self._read_json()
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            self._error(f"JSON inválido: {exc}")
            return

        if path == "/api/demo":
            directory = data.get("directory") or "sandbox_web"
            try:
                created = criar_sandbox(directory)
                target = Path(directory).expanduser()
                # lista os arquivos criados
                files = []
                if target.exists():
                    for item in sorted(target.iterdir()):
                        if item.is_file():
                            files.append(item.name)
                self._send_json({"directory": str(target), "files": files})
            except Exception as exc:  # noqa: BLE001
                self._error(str(exc), status=HTTPStatus.INTERNAL_SERVER_ERROR)
            return

        if path in ("/api/scan", "/api/apply"):
            target = _default_target(data.get("target"))
            config_path = data.get("config")
            try:
                from .config import load_config
                config = load_config(config_path) if config_path else load_config(None)
            except Exception as exc:  # noqa: BLE001
                self._error(f"configuração inválida: {exc}")
                return
            options = _options_from(data)
            state_dir = _state_dir()
            try:
                plan = build_plan(target, config=config, options=options, state_dir=state_dir)
            except CaosZeroError as exc:
                self._error(str(exc))
                return
            except Exception as exc:  # noqa: BLE001
                self._error(str(exc), status=HTTPStatus.INTERNAL_SERVER_ERROR)
                return

            if path == "/api/scan":
                self._send_json(_plan_to_dict(plan))
                return

            # apply
            apply_flag = bool(data.get("apply", True))
            dry_run = not apply_flag
            logger = configure_logging(state_dir, verbose=bool(data.get("verbose", False)))
            journal = Journal(state_dir)
            from .executor import execute_plan as _exec
            result = _exec(plan, journal, logger, dry_run=dry_run)
            run = result.run
            report_path = None
            if data.get("report") and not dry_run:
                from .reporter import write_report
                from pathlib import Path as _P
                rp = data.get("report")
                if rp == "auto":
                    rp = str(state_dir / "reports" / f"relatorio-{run.id}.md")
                report_path = write_report(run, _P(rp).expanduser())
            payload = {
                "mode": "simulacao" if dry_run else "execucao",
                "run_id": run.id,
                "dry_run": dry_run,
                "counts": run.counts(),
                "by_category": run.by_category(),
                "moved": result.moved,
                "failed": result.failed,
                "undone": result.undone,
                "undo_failed": result.undo_failed,
                "operations": [op.to_dict() for op in run.operations],
                "warnings": run.warnings,
                "report": str(report_path) if report_path else None,
            }
            self._send_json(payload)
            return

        if path == "/api/undo":
            state_dir = _state_dir()
            logger = configure_logging(state_dir, verbose=False)
            journal = Journal(state_dir)
            run_id = data.get("run_id")
            latest = bool(data.get("latest", True))
            runs = journal.list_runs()
            if not runs:
                self._error("Nenhuma execução registrada.")
                return
            if run_id:
                run = journal.load(run_id)
            else:
                run = runs[-1] if latest else runs[-1]
            if run.dry_run:
                self._error("Uma simulação não pode ser desfeita.")
                return
            from .executor import undo_run as _undo
            result = _undo(run, journal, logger, dry_run=False)
            self._send_json({
                "run_id": run.id,
                "undone": result.undone,
                "undo_failed": result.undo_failed,
                "operations": [op.to_dict() for op in result.run.operations],
            })
            return

        self._error(f"Endpoint desconhecido: {path}", status=HTTPStatus.NOT_FOUND)

    def log_message(self, format, *args):  # noqa: A003
        LOGGER.debug(format, *args)


def _state_dir() -> Path:
    from .config import default_state_dir
    return default_state_dir()


def run_web(host: str = "127.0.0.1", port: int = 8765, open_browser: bool = True) -> int:
    """Sobe o servidor web e (opcionalmente) abre o navegador."""
    ui = _ui_dir()
    if not ui.exists():
        raise CaosZeroError(f"Pasta de interface não encontrada: {ui}")

    httpd = ThreadingHTTPServer((host, port), CaosZeroHandler)
    url = f"http://{host}:{port}/"
    print(f"CaosZero web em {url}")
    print("Pressione Ctrl+C para encerrar.")

    if open_browser:
        threading.Timer(0.6, lambda: webbrowser.open(url + "layout-12-dualtree-classic.html")).start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nEncerrado.")
    finally:
        httpd.server_close()
    return 0
