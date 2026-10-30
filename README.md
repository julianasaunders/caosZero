# CaosZero 🗂️⚡

> Projeto Integrador da disciplina de **Sistemas Operacionais**.

---

## 📋 1. Objetivo do Projeto

O **CaosZero** é uma aplicação leve desenvolvida em linha de comando (CLI) com foco na automação de tarefas administrativas em ambiente Linux. O objetivo principal do projeto é solucionar o problema de desorganização de diretórios (como a pasta `Downloads` ou áreas de trabalho abarrotadas), demonstrando na prática conceitos fundamentais de Sistemas Operacionais por meio da manipulação de arquivos, gerenciamento de diretórios, uso de variáveis de ambiente e automação via shell script.

---

## 👥 2. Integrantes do Grupo

* Juliana Saunders;
* Jaquelline Feitoza.

---

## 🛠️ 3. Tecnologias Utilizadas

* **Linguagem:** Python 3 (Bibliotecas nativas: `os`, `shutil`, `sys`, `datetime`)
* **Automação:** Bash / Shell Script (`.sh`)
* **Ambiente de Testes:** Linux / Ubuntu (ou distribuições compatíveis)
* **Versionamento:** Git e GitHub

---

## ⚙️ 4. Conceitos de Sistemas Operacionais Aplicados

O projeto implementa e demonstra diretamente os seguintes conceitos estudados na disciplina:

1. **Manipulação de Arquivos e Diretórios (File System):** 
   O programa percorre a árvore de diretórios utilizando chamadas do sistema operacional para varrer itens, verificar a existência de pastas (`os.path.exists`), criar dinamicamente novos diretórios de categoria (`os.makedirs`) e realizar a movimentação física dos arquivos (`shutil.move`).
2. **Gerenciamento de Entradas, Saídas e Logs Operacionais:** 
   O sistema mantém um registro de auditoria (`caoszero.log`), escrevendo interações de escrita em disco em tempo de execução para rastrear todas as operações realizadas pelo usuário ou pelo script automatizado.
3. **Automação de Tarefas e Variáveis de Ambiente:** 
   Utilização de scripts em Shell (`Bash`) para configurar o ambiente de execução, aceitar parâmetros de diretório personalizados de forma dinâmica via argumentos posicionais e preparar o ambiente de testes de forma automatizada.

---

## 🚀 5. Funcionalidades Implementadas

* **Classificação Automática por Extensão:** Identifica e separa arquivos em pastas específicas (`Documentos`, `Imagens`, `Vídeos`, `Compactados`, etc.).
* **Tratamento de Caminhos Flexíveis:** Permite organizar tanto o diretório atual quanto qualquer pasta específica informada via terminal.
* **Geração de Log de Auditoria:** Cria um histórico detalhado contendo a data, hora e a ação realizada em cada arquivo movido.
* **Ambiente de Sandbox para Testes:** Script auxiliar integrado que gera arquivos simulados para validação segura do funcionamento da ferramenta.
* **Compatibilidade Multiplataforma:** Funciona em Linux e Windows, com scripts específicos para cada sistema.

---

## 🪟 6. Como executar em Linux e Windows

### Linux/macOS

```bash
chmod +x automacao.sh test_ambiente.sh
./automacao.sh
./test_ambiente.sh
```

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy Bypass -File .\automacao.ps1
powershell -ExecutionPolicy Bypass -File .\test_ambiente.ps1
```

Também é possível executar o script principal diretamente:

```bash
python caoszero.py .
```

---

## 📂 7. Estrutura do Repositório

```text
caosZero/
├── caoszero.py            # Código-fonte principal da aplicação (CLI)
├── automacao.sh           # Script Bash para execução automatizada
├── automacao.ps1          # Equivalente em PowerShell para Windows
├── test_ambiente.sh       # Cria um ambiente de testes simulado (Linux)
├── test_ambiente.ps1      # Cria um ambiente de testes simulado (Windows)
├── index.html             # Página de apresentação do projeto
├── styles.css             # Estilos da página
├── script.js              # Interações da página
├── .gitignore             # Arquivos ignorados pelo Git
└── README.md              # Documentação oficial do projeto
```

---

## 📂 Materiais do repositório

| Arquivo | O que apresenta |
|---|---|
| [🐍 caoszero.py](caoszero.py) | Aplicação CLI que organiza arquivos por categoria e grava o log de auditoria. |
| [🐚 automacao.sh](automacao.sh) · [🪟 automacao.ps1](automacao.ps1) | Scripts de execução automatizada no Linux e no Windows. |
| [🧪 test_ambiente.sh](test_ambiente.sh) · [🧪 test_ambiente.ps1](test_ambiente.ps1) | Geram um ambiente de testes com arquivos simulados. |
| [🌐 index.html](index.html) · [🎨 styles.css](styles.css) · [⚡ script.js](script.js) | Página de apresentação do projeto. |

---

## 🔗 Projeto relacionado

Desenvolvido para a disciplina de **Sistemas Operacionais**:

- [📚 Repositório da disciplina](https://github.com/julianasaunders/sistemas-operacionais)

---

*Projeto Integrador — Fatec Itapetininga · 2026*
