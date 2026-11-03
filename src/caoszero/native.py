"""Aplicação nativa do CaosZero (janela WebView2 no Windows).

Usa o mesmo layout web (ui/layout-12-dualtree-classic.html) e o mesmo
servidor local (web.py), exibido em uma janela nativa via pywebview. As
operações de arquivo são feitas pelo backend Python, através da API JSON.
"""

from __future__ import annotations

import socket
import threading
import time
import webbrowser

from .errors import CaosZeroError
from .web import run_web as _run_web_unused  # noqa: F401


def _free_port(host: str = "127.0.0.1") -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, 0))
        return s.getsockname()[1]


def run_native(host: str = "127.0.0.1", port: int | None = None) -> int:
    try:
        import webview
    except ImportError as exc:
        raise CaosZeroError(
            "pywebview não está instalado. Instale com: pip install pywebview"
        ) from exc

    if port is None:
        port = _free_port(host)

    # Sobe o servidor HTTP em uma thread separada.
    from .web import CaosZeroHandler
    from http.server import ThreadingHTTPServer

    httpd = ThreadingHTTPServer((host, port), CaosZeroHandler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()

    url = f"http://{host}:{port}/layout-12-dualtree-classic.html"
    # aguarda o servidor responder
    for _ in range(50):
        try:
            import urllib.request
            urllib.request.urlopen(url, timeout=1)
            break
        except Exception:  # noqa: BLE001
            time.sleep(0.1)

    window = webview.create_window(
        "CaosZero 2.0",
        url,
        width=1180,
        height=820,
        resizable=True,
        min_size=(900, 600),
    )

    try:
        webview.start(debug=False)
    finally:
        httpd.shutdown()
        httpd.server_close()
    return 0
