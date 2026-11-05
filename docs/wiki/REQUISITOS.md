# caosZero - Requisitos

## Requisitos Funcionais (RF)

### RF01 - Varrer e Categorizar Diretórios
O sistema deve varrer o diretório alvo (com opção recursiva `-r` para subdiretórios) e classificar os arquivos por categoria com base na extensão (Documentos, Imagens, Vídeos, Músicas, Planilhas, Compactados, Instaladores, Código e Outros).

### RF02 - Filtrar, Renomear e Arquivar
Deve permitir filtragem por padrão de nome (`--pattern`), idade (`--older-than`), tamanho (`--min-size` e `--max-size`) e categoria (`--category`), além de suportar renomeação em massa (`--rename`) e arquivamento de itens antigos por ano (`--archive-old`).

### RF03 - Simulação por Padrão (Dry-run)
O aplicativo deve simular a organização por padrão, exibindo a prévia do plano de operações sem modificar nada no disco.

### RF04 - Execução Real
Alterações reais no sistema de arquivos só devem ocorrer com o parâmetro `--apply`, solicitando confirmação interativa do usuário (ou ignorando a confirmação com `--yes`).

### RF05 - Journaling e Reversão (Undo)
O sistema deve registrar cada operação em um arquivo de histórico (journal) em JSON e permitir desfazer a última execução através do comando `undo`.

### RF06 - Geração de Relatórios
Deve gerar relatórios de execução nos formatos Markdown (`.md`), CSV (`.csv`) e JSON (`.json`).

### RF07 - Diagnóstico do Sistema
O comando `doctor` deve coletar e exibir diagnósticos dos recursos e limites do sistema operacional (processo, CPU, memória, disco e permissões).

### RF08 - Configuração e Modo Interativo
Deve ler configurações personalizadas a partir de arquivos JSON e oferecer uma interface CLI interativa orientada por menu.

---

## Requisitos Não Funcionais (RNF)

### RNF01 - Segurança e Integridade
- Não deve excluir nem sobrescrever arquivos existentes.
- O sistema deve recusar operações na raiz do SO (`/` ou `C:\`).
- Deve ignorar links simbólicos.

### RNF02 - Portabilidade e Independência
O aplicativo deve ser compatível com Linux e Windows utilizando Python 3.10+, sem exigência de dependências externas obrigatórias (utilizando apenas a biblioteca padrão).

### RNF03 - Confiabilidade e Testabilidade
O código deve manter cobertura de testes automatizados integrados a pipelines de integração contínua (CI em Ubuntu e Windows).

### RNF04 - Auditabilidade e Observabilidade
Manter logs de auditoria com data/hora e histórico incremental de execuções totalmente auditáveis e reversíveis.