# ellocene-ops — Base Canónica do Squad

Repositório canónico de operação do squad **ellocene-ops** (holding Ellocene).

## Protocolo LER PRIMEIRO (versão MCP 2.0)
1. Ler `00_INDEX.md` pelo **conector GitHub** (`get_file_contents`, `owner="Altars-Group"`, `repo="ellocene-ops"`).
2. Ler o índice da área aplicável em `01_Knowledge/<area>/` pelo mesmo conector.
3. Processos/registos/decisões → **conector Fibery**.
4. Só depois agir. Se o conector falhar, reportar com o **erro cru** — não improvisar de memória, e **nunca parar por causa de um `git pull`** (a VM saiu do caminho crítico).

## Estrutura
| Pasta | Conteúdo |
|---|---|
| `00_Governanca/` | Regras, decisões da holding |
| `01_Knowledge/` | Base de conhecimento por área (obras shardadas) |
| `02_Tarefas/` | Estado da fila de tarefas |
| `03_Processos/` | Processos repetíveis (inventário E2) |
| `04_Projetos/` | Documentos de projecto |
| `05_Outbox/` | Entregáveis prontos a publicar |
| `06_Arquivo/` | Histórico |

## Acesso
**Canal canónico:** conector GitHub (MCP) para operação + conector Fibery (MCP) para registo.
Deploy key SSH na VM: **fora do caminho crítico** (P3) — ver `DEPLOY-KEY.md`.
