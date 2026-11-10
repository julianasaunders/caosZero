# Interfaces do CaosZero (protótipos)

Vinte e dois layouts alternativos para a interface gráfica do CaosZero, inspirados
na estética do CleanMyMac (hero roxo, botões em pílula, cartões arredondados,
tipografia limpa), nas cores do Dark Dashboard e nos recursos do DropIt e do
Kimi Work (perfis, associações, filtros, ações, prompt em linguagem natural,
plano de revisão, agendamento). Todos são arquivos HTML autocontidos, com
simulação em JavaScript, sem backend.

## Primeira rodada

| Arquivo | Estilo |
| --- | --- |
| `layout-1-cleanmymac.html` | CleanMyMac Classic — hero roxo, cards, passos, conceitos de SO |
| `layout-2-dark-dashboard.html` | Dark Dashboard — sidebar, dropzone, log ao vivo, tiles |
| `layout-3-minimal-card.html` | Minimal Card — um cartão central, anel de progresso |
| `layout-4-gradient-glass.html` | Gradient Glass — gradiente roxo→azul, cartões de vidro |
| `layout-5-terminal-modern.html` | Terminal Modern — estética de terminal com acentos verdes |

## Segunda rodada — terminal + minimal + glass

| Arquivo | Estilo |
| --- | --- |
| `layout-6-terminal-minimal.html` | Terminal Minimal — cartão central escuro + anel + chips + log |
| `layout-7-glass-terminal.html` | Glass Terminal — painéis de vidro sobre gradiente + log + conceitos |
| `layout-8-command-palette.html` | Command Palette — paleta estilo Spotlight, lista de ações e atalhos |
| `layout-9-split-terminal.html` | Split Terminal — terminal/log à esquerda, modos e conceitos à direita |
| `layout-10-neon-terminal.html` | Neon Terminal — brilho neon verde/roxo, cartões de vidro com glow |
| `layout-11-centered-terminal.html` | Centered Terminal — painel único centralizado, dropzone com árvore |

## Terceira rodada — drag-and-drop com árvore dupla

| Arquivo | Estilo |
| --- | --- |
| `layout-12-dualtree-classic.html` | Dual Tree Classic — dropzone + duas árvores lado a lado (antes/depois) |
| `layout-13-dualtree-compact.html` | Dual Tree Compact — versão densa e compacta, fonte pequena |
| `layout-14-dualtree-neon.html` | Dual Tree Neon — brilho neon verde/roxo, cartões de vidro com glow |
| `layout-15-dualtree-splitpanels.html` | Dual Tree Split Panels — entrada à esquerda, saída planejada à direita |
| `layout-16-dualtree-terminallog.html` | Dual Tree Terminal Log — estética de terminal, árvores como blocos de código |

## Quarta rodada — baseado em DropIt + Kimi AI

| Arquivo | Estilo |
| --- | --- |
| `layout-17-dropit-kimi-hybrid.html` | DropIt + Kimi Hybrid — perfis, regras, prompt NL, plano de revisão, agendamento |
| `layout-18-kimi-work.html` | Kimi Work Style — gradientes, glass, prompt NL, plano de revisão |
| `layout-19-dropit-pro.html` | DropIt Pro — desktop-app: perfis, associações, filtros, ações, progress window |

## Quinta rodada — DropIt explicativo

| Arquivo | Estilo |
| --- | --- |
| `layout-20-dropit-explained.html` | DropIt Explained — passo a passo numerado, associações explicadas, ícone flutuante |
| `layout-21-dropit-wizard.html` | DropIt Wizard — assistente em 4 passos: pasta → regras → revisar → executar |
| `layout-22-dropit-dashboard.html` | DropIt Dashboard — dashboard explicativo: perfis, associações, filtros, funcionalidades, IA, agendamento |

Abra `index.html` para ver a galeria e escolher um layout. Após a escolha, o
layout selecionado será integrado à aplicação (backend Python, persistência de
configuração e empacotamento).