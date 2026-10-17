# Convenção Única da Base de Conhecimento — squad ellocene-ops

**Versão:** 1.0 · **Data:** 2026-10-16 · **Autor:** Bibliotecário (Tiv) · **Tarefa:** TASK-2026-10-16-007
**Estado:** PROPOSTA — requer ratificação do CTO (estrutura) e dos donos de área (migração)

> Este é o formato **único** que toda a área de conhecimento segue. Foi derivado do que já existe
> (não inventado de raiz): adopta a convenção que o remoto já usa e que o `00_INDEX.md` da raiz fixa
> como alvo, e propõe a migração explícita do que desvia.

---

## 1. Estrutura de pastas (uma só, para todas as áreas)

```
01_Knowledge/
├── 00_INDEX.md                      # índice-mestre (raiz de 01_Knowledge) — mapa das áreas
├── _CATALOGO.md                     # catálogo global de obras (adquiridas + shardadas)
├── _CATALOGO.csv                    # versão máquina-legível
├── _meta/                           # scripts, cadência, staging, logs (NÃO é conhecimento)
│   ├── acquire_knowledge.py         # pipeline de aquisição (cópia ÚNICA)
│   ├── daily_acquire.sh             # cadência diária
│   ├── CADENCIA.md
│   ├── _staging/<area>/             # originais descarregados (epub/pdf) antes de shardar
│   └── _logs/                       # logs de aquisição + gaps.md
├── <area>/                          # minúsculas, sem acentos
│   ├── 00_INDEX.md                  # índice da área (obrigatório)
│   └── <obra-slug>/                 # UMA subpasta por obra
│       ├── 00_INDEX.md              # índice da obra (obrigatório)
│       └── NN-<capitulo-slug>.md    # 1 ficheiro por capítulo
```

**Regras de caminho:**
- `<area>`: **minúsculas, sem acentos, sem espaços** (`marketing`, `governanca`, `financas`). Nunca `Marketing`/`Governança`.
- `<obra-slug>`: `autor-ano-titulo-curto` em minúsculas, ex.: `barnum-1880-the-art-of-money-getting`.
- `<capitulo-slug>`: `NN-titulo-curto`, `NN` com 2 dígitos (`01`, `02`, …). Ex.: `01-golden-rules-for-making-money.md`.
- Separador: **hífen** (`-`). Nunca underscore no nome de ficheiro de conteúdo (underscore fica reservado para meta/scripts).

### Áreas canónicas (v1 — a ratificar pelo CTO)

Proposta de **9 áreas** (a taxonomia do `00_INDEX.md` da raiz, que é a mais completa e já tem donos atribuídos):

| Área | Dono (Tiv) |
|---|---|
| `financas` | CFO |
| `marketing` | CMO |
| `negocios` | CEO |
| `processos` | Processos |
| `pessoas` | CHRO |
| `receita` | CRO |
| `legal` | Legal |
| `governanca` | Governança |
| `tecnologia` | CTO |

> **Conflito a resolver:** o `00_INDEX.md` do remoto (versão DevOps) propõe 6 áreas diferentes
> (`Governanca`, `Financeiro`, `Tecnologia`, `Operacoes`, `Marketing`, `Clientes`). **Duas taxonomias
> concorrentes não podem coexistir.** Recomendação: adoptar as 9 áreas (já têm donos e índices criados)
> e mapear as 6 do remoto para elas (`Financeiro`→`financas`, `Operacoes`→`processos`,
> `Clientes`→`receita`/`marketing`). Decisão do CTO + Guardião.

---

## 2. Front-matter obrigatório (por shard)

Todo o ficheiro de capítulo começa com este bloco YAML:

```yaml
---
title: "Título do Capítulo"
author: "Autor da Obra"
slug: "obra-slug"
chapter: "CH01"
slug_cap: "ch01-titulo-curto"
area: "negocios"
source: "https://www.gutenberg.org/ebooks/XXXX"
license: "Public domain (Project Gutenberg)"
shard_of: "titulo-completo-da-obra"
---
```

**Campos obrigatórios:** `title`, `author`, `slug`, `chapter`, `area`, `source`, `license`.
**Campos recomendados:** `slug_cap`, `shard_of`, `year`.

**Regras de licença:** só entram obras em **domínio público**, **CC0**, **CC BY / BY-SA / BY-ND** ou
**open access**. Licença restritiva → recusada e registada em `_meta/_logs/gaps.md` (nome da obra,
autor, porquê). Nunca se preenche uma lacuna com estimativa.

---

## 3. Formato do `00_INDEX.md` de área

Estrutura fixa (adaptada do índice de `negocios/`, que é o mais completo):

```markdown
# 01_Knowledge/<area> — Índice da Área

**Área:** <area> · **Dono:** <Tiv> · **Estado:** v<X.Y> (<data>)

## O que vive aqui
Uma frase sobre o âmbito da área.

## Convenção de ficheiros
`01_Knowledge/<area>/<obra-slug>/NN-<capitulo-slug>.md`

## Índice de obras

### <Título da Obra> (<Autor>, <ano>)
*Autor: … · <ano> · N ficheiros · Fonte: <url> · Licença: <licença>*

- [01 — <Título>](<obra-slug>/01-titulo.md)
- [02 — <Título>](<obra-slug>/02-titulo.md)

## Lacunas declaradas
- <obra essencial sem edição aberta> — motivo.

## Como usar
1. Ler a base pelo **conector GitHub** (`get_file_contents`, `owner="Altars-Group"`, `repo="ellocene-ops"`) — não por `git pull` na VM.
2. Ler este índice.
3. Abrir o capítulo que interessa.
```

**Regras do índice:**
- **Zero links mortos**: cada link do índice aponta para um ficheiro que existe.
- **Zero órfãos**: cada shard é referenciado no índice da área.
- **Lacunas declaradas**: obras essenciais que não têm edição aberta são listadas com o motivo, para que ninguém as procure de novo.
- O `00_INDEX.md` de **obra** (dentro da subpasta) segue o mesmo formato, ao nível da obra.

---

## 4. Catálogo global

`_CATALOGO.md` (e `.csv`) deve ligar **aquisição** e **sharding**:

| Título | Autor | Ano | Área | Fonte | Licença | Original (staging) | Shards | Estado |

Estados: `descarregada` → `shardada` → `publicada`. Hoje o catálogo só tem `descarregada`;
tem de passar a incluir as obras shardadas por outros Tivs.

---

## 5. Migrações necessárias (lista explícita)

Nenhuma destas migrações foi executada — requerem decisão do dono da área.

| # | Migração | De | Para | Dono da decisão |
|---|---|---|---|---|
| M1 | `negocios/` ficheiros planos → subpastas por obra | `negocios/The-Art-of-Money-Getting_CH07.md` | `negocios/barnum-1880-the-art-of-money-getting/07-…​.md` | **CEO** |
| M2 | Capitalização de áreas | `Marketing/`, `Governanca/` | `marketing/`, `governanca/` | CTO/DevOps |
| M3 | Unificar pipeline | `_meta/` **e** `_scripts/` (2 cópias) | só `_meta/` | Bibliotecário |
| M4 | Alinhar VM com remoto (pull) | VM congelada | VM = remoto | DevOps |
| M5 | Alinhar taxonomia de áreas (9 vs 6) | duas listas | 9 áreas | CTO/Guardião |
| M6 | Alinhar estrutura de topo (remoto vs VM) | `02_Control`/`04_Execution` vs `02_Processes`/`03_Workflows`/`06_Governance` | uma só | CTO/DevOps |
| M7 | Catálogo incluir obras shardadas | 7 obras | todas as obras | Bibliotecário |
| M8 | Corrigir nome do timer no `00_INDEX.md` | `ellocene-sync.timer` | `ellocene-ops-sync.timer` | Bibliotecário |

---

## 6. Regras de operação (resumo)

1. **LER PRIMEIRO (v2.0/MCP)**: ler `00_INDEX.md` raiz pelo conector GitHub → ler índice da área → só depois agir. Se o conector falhar, reportar com o erro cru (nunca parar por causa de um `git pull`).
2. **Prova lida de volta**: nada se declara feito sem ler o resultado. O que está publicado é o que o Credo lê.
3. **Não inventar**: obra sem edição aberta verificável → lacuna registada, não estimada.
4. **Fronteira de donos**: não se altera nem move ficheiro de outra área sem o dono decidir.
5. **Fronteira de fontes**: GitHub = operação (conhecimento, processos em ficheiro, workflows, agentes, tarefas, outputs). Fibery = registo (processos formais, decisões, governança, KPI).
