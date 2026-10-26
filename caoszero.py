import os
import shutil
from datetime import datetime

# Mapeamento de extensoes para pastas de destino
CATEGORIAS = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Compactados": [".zip", ".tar.gz", ".rar", ".7z"],
    "Executaveis_Scripts": [".sh", ".py", ".bin", ".deb"]
}

LOG_FILE = "caoszero.log"

def registrar_log(mensagem):
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{data_hora}] {mensagem}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(linha)

def organizar_diretorio(diretorio_alvo):
    if not os.path.exists(diretorio_alvo):
        print(f"Erro: O diretorio '{diretorio_alvo}' nao existe.")
        return

    print(f"--- Iniciando CaosZero em: {diretorio_alvo} ---")
    registrar_log(f"Iniciada organizacao no diretorio: {diretorio_alvo}")

    arquivos_movidos = 0

    for item in os.listdir(diretorio_alvo):
        caminho_item = os.path.join(diretorio_alvo, item)

        # Ignora se for diretorio ou o arquivo de log
        if os.path.isdir(caminho_item) or item == LOG_FILE:
            continue

        nome, extensao = os.path.splitext(item)
        extensao = extensao.lower()

        # Identifica a categoria
        categoria_destino = "Outros"
        for categoria, extensoes in CATEGORIAS.items():
            if extensao in extensoes:
                categoria_destino = categoria
                break

        # Cria a pasta de destino se nao existir (Conceito SO: Manipulacao de Diretorios)
        pasta_destino = os.path.join(diretorio_alvo, categoria_destino)
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        # Mover o arquivo (Conceito SO: Gerenciamento de Arquivos)
        caminho_destino = os.path.join(pasta_destino, item)
        shutil.move(caminho_item, caminho_destino)
        
        log_msg = f"Movido: {item} -> {categoria_destino}/"
        print(log_msg)
        registrar_log(log_msg)
        arquivos_movidos += 1

    print(f"\nConcluido! Total de arquivos organizados: {arquivos_movidos}")
    registrar_log(f"Finalizado. Total de arquivos movidos: {arquivos_movidos}")

if __name__ == "__main__":
    import sys
    # Permite passar o caminho como argumento ou usa a pasta atual
    alvo = sys.argv[1] if len(sys.argv) > 1 else "."
    organizar_diretorio(alvo)