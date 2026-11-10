# -*- coding: utf-8 -*-
"""Entry point para o executável gráfico do CaosZero (sem console)."""

import sys
from pathlib import Path

src = Path(__file__).resolve().parent / "src"
if str(src) not in sys.path:
    sys.path.insert(0, str(src))

from caoszero.native import run_native

if __name__ == "__main__":
    raise SystemExit(run_native())
