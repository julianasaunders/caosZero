$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pastaTeste = Join-Path $scriptDir "sandbox_teste"

New-Item -ItemType Directory -Force -Path $pastaTeste | Out-Null

@(
    "relatorio.pdf",
    "foto_ferias.jpg",
    "video_aula.mp4",
    "backup.zip",
    "notas.txt",
    "dados.csv"
) | ForEach-Object {
    $arquivo = Join-Path $pastaTeste $_
    New-Item -ItemType File -Force -Path $arquivo | Out-Null
}

Write-Host "Ambiente de teste criado na pasta '$pastaTeste' com 6 arquivos variados."
