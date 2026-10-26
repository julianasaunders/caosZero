#!/bin/bash

# Cria pasta de teste
PASTA_TESTE="sandbox_teste"
mkdir -p "$PASTA_TESTE"

# Gera arquivos ficticios
touch "$PASTA_TESTE/relatorio.pdf"
touch "$PASTA_TESTE/foto_ferias.jpg"
touch "$PASTA_TESTE/video_aula.mp4"
touch "$PASTA_TESTE/backup.zip"
touch "$PASTA_TESTE/notas.txt"
touch "$PASTA_TESTE/dados.csv"

echo "Ambiente de teste criado na pasta '$PASTA_TESTE' com 6 arquivos variados."