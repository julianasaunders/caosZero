#!/bin/bash

# Script de automacao para o CaosZero
PASTA_TARGET="${1:-$HOME/Downloads}"

echo "=========================================="
echo "      CaosZero - Execucao Automatica      "
echo "=========================================="
echo "Diretorio alvo: $PASTA_TARGET"

# Verifica se o Python 3 esta instalado
if ! command -v python3 &> /dev/null; then
    echo "Erro: Python3 nao instalado."
    exit 1
fi

# Executa o script Python
python3 src/caoszero.py "$PASTA_TARGET"

echo "Operacao finalizada com sucesso."