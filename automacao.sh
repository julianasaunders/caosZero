#!/bin/bash

# Script de automacao para o CaosZero (Linux/macOS)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PASTA_TARGET="${1:-$HOME/Downloads}"
PYTHON_CMD="python3"

if ! command -v "$PYTHON_CMD" >/dev/null 2>&1; then
    PYTHON_CMD="python"
fi

if ! command -v "$PYTHON_CMD" >/dev/null 2>&1; then
    echo "Erro: Python nao encontrado no PATH."
    exit 1
fi

echo "=========================================="
echo "      CaosZero - Execucao Automatica      "
echo "=========================================="
echo "Diretorio alvo: $PASTA_TARGET"

echo "Usando Python: $(command -v "$PYTHON_CMD")"
"$PYTHON_CMD" "$SCRIPT_DIR/caoszero.py" "$PASTA_TARGET"

echo "Operacao finalizada com sucesso."