param(
    [string]$PastaTarget = "$HOME\Downloads"
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonCmd = ""

if (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCmd = "py"
}
elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCmd = "python"
}
elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
    $pythonCmd = "python3"
}
else {
    Write-Error "Python nao encontrado no PATH."
    exit 1
}

Write-Host "=========================================="
Write-Host "      CaosZero - Execucao Automatica      "
Write-Host "=========================================="
Write-Host "Diretorio alvo: $PastaTarget"
Write-Host "Usando Python: $pythonCmd"

& $pythonCmd (Join-Path $scriptDir "caoszero.py") $PastaTarget

Write-Host "Operacao finalizada com sucesso."
