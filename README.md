# CaosZero 2.0

**Automatizador de tarefas com arquivos** — projeto integrador da disciplina de
**Sistemas Operacionais**.

O CaosZero organiza pastas por categoria, renomeia arquivos em massa, arquiva
itens antigos, gera relatórios e permite **desfazer** a última execução. A
interface principal é um aplicativo nativo para Windows, que seleciona a
pasta, analisa e aplica a organização diretamente no seu computador.

[![CI](https://github.com/julianasaunders/caosZero/actions/workflows/ci.yml/badge.svg)](https://github.com/julianasaunders/caosZero/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Licença MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-green.svg)](LICENSE) [![Demonstração](https://img.shields.io/badge/DEMO-online-blue.svg)](https://julianasaunders.github.io/caosZero/)

> **Demonstração online:** https://julianasaunders.github.io/caosZero/

> **Segurança em primeiro lugar:** por padrão o CaosZero apenas **simula** a
> organização. Nenhum arquivo é alterado sem sua confirmação explícita.
> Nenhum arquivo é excluído ou sobrescrito.

---

## Interface gráfica (principal)

> O CaosZero é, antes de tudo, um **aplicativo com interface gráfica**.
> Você não precisa saber programar — basta abrir e clicar.

### 🚀 Como usar (em 5 passos)

| Passo | Ação | O que acontece |
| :---: | --- | --- |
| 1️⃣ | **Abrir** `CaosZero.exe` | A janela do app aparece |
| 2️⃣ | **Selecionar pasta** | Escolha a pasta que deseja organizar |
| 3️⃣ | **Analisar** | O CaosZero planeja tudo e mostra a árvore **Antes/Depois** + log + estatísticas. **Nada é alterado.** |
| 4️⃣ | **Aplicar organização** | Botão flutuante com confirmação antes de mover qualquer arquivo |
| 5️⃣ | **Desfazer** | Restaura a última execução com um clique |

### ✨ Recursos da interface

| Recurso | Descrição |
| --- | --- |
| 📂 **Selecionar pasta** | Seletor nativo de pastas do Windows |
| 🔍 **Analisar** | Planeja as operações e exibe a árvore "Antes/Depois" |
| ✅ **Aplicar organização** | Botão flutuante com confirmação antes de mover |
| ↩️ **Desfazer** | Restaura a última execução |
| 🌙/☀️ **Modo claro/escuro** | Alternável pelo ícone de sol/lua no cabeçalho |
| 📋 **Plano de revisão** | Revise antes de aplicar |
| 🩺 **Diagnóstico** | CPU, memória, disco, permissões |

> **O executável está em** `dist/CaosZero.exe` (ou `Downloads/CaosZero.exe`).

> **Também disponível** como página web em `ui/app.html`.

---

## Demonstração

> **Acesse a demonstração online:**
> https://julianasaunders.github.io/caosZero/

A demonstração apresenta o CaosZero 2.0, seus recursos, o fluxo de
organização e os conceitos de Sistemas Operacionais aplicados.

## Sumário

- [Interface gráfica (principal)](#interface-gráfica-principal)
- [Demonstração](#demonstração)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Como funciona](#como-funciona)
- [Conceitos de Sistemas Operacionais](#conceitos-de-sistemas-operacionais)
- [Automação e agendamento](#automação-e-agendamento)
- [Configuração](#configuração)
- [Testes](#testes)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Documentação](#documentação)
- [Comunidade e segurança](#comunidade-e-segurança)
- [Equipe](#equipe)
- [Licença](#licença)

---

## Funcionalidades

- **Organização por extensão** com categorias configuráveis.
- **Simulação segura** por padrão — nada é alterado sem confirmação.
- **Filtros**: glob, idade, tamanho, categoria, subdiretórios e ocultos.
- **Renomeação em massa** com `{name}`, `{ext}`, `{seq}`, `{date}` e `{categoria}`.
- **Arquivamento de antigos** em `Arquivo/AAAA/`.
- **Journal em JSON** de cada execução.
- **Undo** da última execução (ou de um ID específico).
- **Relatórios** em Markdown, CSV e JSON.
- **Diagnóstico do SO** (`doctor`): processo, CPU, memória, disco, permissões,
  variáveis de ambiente e limites de cgroup.
- **Modo interativo** para uso guiado.
- **Scripts** de automação para Bash e PowerShell.
- **Sem dependências externas** para executar.
- **Interface nativa** para Windows.
- **Modo claro/escuro** alternável.

---

## Instalação

### Requisitos

- Python **3.10** ou superior (para desenvolvimento).
- Windows, Linux ou macOS.

### Usar o aplicativo (usuário final)

Baixe `CaosZero.exe` (em `dist/` ou `Downloads/`) e abra com duplo clique.
Não é necessário instalar Python.

### Usar do repositório (desenvolvimento)

```bash
git clone https://github.com/julianasaunders/caosZero.git
cd caosZero
```

### Ambiente virtual (recomendado para desenvolvimento)

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e .
```

---

## Como funciona

O CaosZero separa **planejamento** e **execução**:

1. **Planejar** — lê metadados, aplica filtros e calcula destinos sem tocar
   no disco. (`planner.py`)
2. **Confirmar** — mostra a prévia, avisos e pede confirmação antes de
   executar. (interface web)
3. **Executar** — move, renomeia ou arquiva e grava cada passo no journal.
   (`executor.py`)
4. **Relatar e desfazer** — gera MD/CSV/JSON e permite restaurar a execução
   anterior. (`reporter.py` · `journal.py`)

Nenhum arquivo é sobrescrito: se o destino já existir, o CaosZero gera um
nome único (`foto.jpg` → `foto (1).jpg`).

---

## Conceitos de Sistemas Operacionais

O projeto demonstra, de forma aplicada:

| Conceito | Onde aparece | Como demonstrar |
| --- | --- | --- |
| **Sistema de arquivos** | `planner.py`, `executor.py` | Prévia com origem e destino |
| **Chamadas de sistema** | `journal.py`, `reporter.py` | Journal JSON gerado |
| **Processos** | `system_info.py` | PID, PPID, threads |
| **CPU** | `system_info.py` | Núcleos, load, cgroup |
| **Memória** | `system_info.py` | Total, disponível, cgroup |
| **Disco** | `system_info.py`, `planner.py` | Total, usado, livre |
| **Permissões** | `system_info.py`, `planner.py` | Modo octal e simbólico |
| **Concorrência** | `utils.py`, `executor.py` | Colisão resolvida com `(1)` |
| **Automação** | `scripts/` | Cron e Agendador |
| **Tolerância a falhas** | `journal.py`, `undo` | Restauração da execução |

---

## Automação e agendamento

### Linux/macOS

```bash
./scripts/automacao.sh --target ~/Downloads --apply --report
./scripts/agendar_cron.sh --target ~/Downloads --time 09:00 --apply
```

### Windows (PowerShell)

```powershell
.\scripts\automacao.ps1 -Target "$HOME\Downloads" -Apply -Report
.\scripts\agendar_tarefa.ps1 -Target "$HOME\Downloads" -Time "09:00" -Register
```

---

## Configuração

A configuração é procurada nesta ordem:

1. `--config CAMINHO`
2. variável `CAOSZERO_CONFIG`
3. `<CAOSZERO_HOME>/config.json`
4. `./config/caoszero.example.json`

O diretório de estado segue o padrão XDG no Linux/macOS e `%LOCALAPPDATA%`
no Windows. A variável `CAOSZERO_HOME` tem precedência em todos os casos.

Variáveis de ambiente: `CAOSZERO_HOME`, `CAOSZERO_CONFIG`, `CAOSZERO_TARGET`.

Exemplo de configuração:

```json
{
  "categories": {
    "Documentos": [".pdf", ".docx", ".txt", ".md"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Compactados": [".zip", ".tar.gz", ".rar", ".7z"]
  },
  "ignore_dirs": [".git", "node_modules", "__pycache__"],
  "max_depth": 5,
  "follow_symlinks": false
}
```

Consulte [`config/caoszero.example.json`](config/caoszero.example.json).

---

## Testes

```bash
python -m unittest discover -s tests -v
```

A suíte cobre configuração, utilitários, planejador, executor, journal, undo,
relatórios, diagnóstico e a interface web.

```bash
python -m unittest tests.test_planner -v
```

---

## Estrutura do projeto

```text
caosZero/
├── src/                        # código-fonte
│   └── caoszero/
│       ├── cli.py                  # interface do aplicativo
│       ├── web.py                  # servidor web local + API JSON
│       ├── native.py               # aplicação nativa (pywebview)
│       ├── config.py               # configuração e diretórios padrão
│       ├── planner.py              # planejamento (sem efeitos colaterais)
│       ├── executor.py             # execução e undo
│       ├── journal.py              # persistência das execuções
│       ├── reporter.py             # relatórios MD/CSV/JSON
│       ├── system_info.py          # diagnóstico do SO
│       ├── models.py               # modelos de domínio
│       ├── utils.py                # utilitários
│       └── demo.py                 # sandbox de demonstração
├── ui/                         # interfaces web (galeria + app.html)
├── tests/                      # testes automatizados
├── scripts/                    # automação, agendamento e hooks
├── config/                     # configuração de exemplo
├── docs/                       # documentação do projeto
├── .github/                    # CI, templates e CODEOWNERS
├── index.html                  # página do projeto (GitHub Pages)
├── caoszero.py                 # atalho para executar sem instalar
├── pyproject.toml              # metadados e entrypoint
├── LICENSE
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
└── README.md
```

---

## Documentação

| Arquivo | Conteúdo |
| --- | --- |
| [`docs/PLANEJAMENTO.md`](docs/PLANEJAMENTO.md) | Escopo, backlog e divisão de tarefas |
| [`docs/ARQUITETURA.md`](docs/ARQUITETURA.md) | Módulos e fluxo de dados |
| [`docs/CONCEITOS-SO.md`](docs/CONCEITOS-SO.md) | Conceitos de SO aplicados ao código |
| [`docs/GUIA-DE-USO.md`](docs/GUIA-DE-USO.md) | Guia de uso completo |
| [`docs/TESTES.md`](docs/TESTES.md) | Estratégia e execução dos testes |
| [`docs/RELEASE.md`](docs/RELEASE.md) | Checklist de release |
| [`docs/DIVISAO-DE-TAREFAS.md`](docs/DIVISAO-DE-TAREFAS.md) | Divisão entre as integrantes |
| [Wiki](https://github.com/julianasaunders/caosZero/wiki) | Páginas de apoio do projeto |

---

## Comunidade e segurança

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — branches, commits, PRs e revisão
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — convivência e colaboração
- [`SECURITY.md`](SECURITY.md) — relato de vulnerabilidades e garantias

---

## Equipe

- **Juliana Saunders** — [@julianasaunders](https://github.com/julianasaunders)
- **Jaquelline Feitoza** — [@jaquellinef](https://github.com/jaquellinef)

---

## Licença

Distribuído sob a licença **MIT**. Veja [`LICENSE`](LICENSE).
