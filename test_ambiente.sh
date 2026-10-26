#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PASTA_TESTE="$SCRIPT_DIR/sandbox_teste"

mkdir -p "$PASTA_TESTE"
for nome in \
  "relatorio.pdf" \
  "foto_ferias.jpg" \
  "video_aula.mp4" \
  "backup.zip" \
  "notas.txt" \
  "dados.csv"
do
  : > "$PASTA_TESTE/$nome"
done

echo "Ambiente de teste criado na pasta '$PASTA_TESTE' com 6 arquivos variados."