# 00_INDEX — Base Canónica do Squad ellocene-ops

**Versão:** 1.0 · **Data:** 2026-10-16 · **Dono:** Guardião · **Estado:** OPERACIONAL
**Repo:** `Altars-Group/ellocene-ops` (privado) · **Clone na VM (leitura de emergência):** `/workspace/ellocene-ops`

> Este é o MAPA e o PROTOCOLO. Todo o Tiv o lê antes de agir.
> Canal canónico: **MCP** (conector GitHub para operação + conector Fibery para registo). Não ages de memória; se o conector falhar, reportas com o erro cru.

---

## 1. Protocolo «LER PRIMEIRO» (obrigatório, todos os Tivs) — versão MCP 2.0

> Decisão do Credo, 17/10: o canal canónico é o **MCP** (conector GitHub + conector Fibery). A VM sai do caminho crítico. Substitui a v1.0 (git pull na VM).

1. Ler este `00_INDEX.md` pelo **conector GitHub**: `connector_call github get_file_contents` com `owner="Altars-Group"`, `repo="ellocene-ops"`, `path="00_INDEX.md"`.
2. Ler o índice da tua área pelo mesmo conector: `path="01_Knowledge/<area>/00_INDEX.md"` (e `path="04_Agents/<o-teu-slug>.md"` quando aplicável).
3. Quando for processo/registo/decisão/governança, ler também pelo **conector Fibery**.
4. Só depois agir. Citar a referência usada (caminho no repo ou id do documento Fibery).
5. Se o conector falhar → reportar com o **erro cru**, não improvisar de memória. Via de recurso: clone local `/workspace/ellocene-ops` **só como leitura de emergência** (pode estar desactualizado). **Nunca parar a operação por causa de um `git pull`.**
6. O system prompt de cada Tiv tem **apenas o PONTEIRO** para este protocolo — o conhecimento lê-se da base em cada run.

**Fronteira de fontes:**
- GitHub (este repo) = OPERAÇÃO (conhecimento, processos em ficheiro, workflows, agentes, tarefas, outputs).
- Fibery = REGISTO (processos formais, decisões, governança, KPI).

---

## 2. Mapa de áreas (dono → caminho canónico)

| Área | Dono (Tiv) | Índice de área |
|---|---|---|
| financas | CFO | `01_Knowledge/financas/00_INDEX.md` |
| marketing | CMO | `01_Knowledge/marketing/00_INDEX.md` |
| negocios | CEO | `01_Knowledge/negocios/00_INDEX.md` |
| processos | Processos | `01_Knowledge/processos/00_INDEX.md` |
| pessoas | CHRO | `01_Knowledge/pessoas/00_INDEX.md` |
| receita | CRO | `01_Knowledge/receita/00_INDEX.md` |
| legal | Legal | `01_Knowledge/legal/00_INDEX.md` |
| governanca | Governança | `01_Knowledge/governanca/00_INDEX.md` |
| tecnologia | CTO | `01_Knowledge/tecnologia/00_INDEX.md` |

---

## 3. Estrutura do repo

```
00_INDEX.md
01_Knowledge/<area>/          ← conhecimento por área (9 áreas)
02_Tarefas/
03_Processos/
04_Projetos/
05_Outbox/
06_Arquivo/
```

---

## 4. Convenções de sharding de conhecimento

`01_Knowledge/<area>/<obra-slug>/NN_<capitulo-slug>.md`

**Regras:**
- `<area>` em minúsculas; sem acentos nos caminhos.
- `<obra-slug>`: slug do título da obra (ex.: `the-art-of-money-getting`).
- `<capitulo-slug>`: slug do título do capítulo (ex.: `ch01-growth-mindset`).
- NN = número do capítulo com zero à esquerda (ex.: `CH01`).

**Cabeçalho obrigatório:**
```markdown
---
title: "Título do Capítulo"
author: "Autor da Obra"
slug: "obra-slug"
chapter: "CH01"
slug_cap: "ch01-growth-mindset"
area: "negocios"
source: "https://..."
license: "CC BY-NC-SA 4.0"
---

# Título do Capítulo
```

---

## 5. Sincronização

**O canal canónico é o MCP; a VM e o Mac são opcionais.**

| Fronteira | Mecanismo | Cadência |
|---|---|---|
| Base ↔ Tivs | **conector GitHub (MCP)** — leitura/escrita da operação | em cada run |
| Registo ↔ Tivs | **conector Fibery (MCP)** — processos, decisões, governança, KPI | em cada run |
| VM ↔ GitHub | `ellocene-sync.timer` → `git pull --ff-only` | **P3 — fora do caminho crítico** |
| GitHub → Drive | GitHub Action agendada | diária |

**Só com telemóvel:** o Credo escreve no GitHub (web/app) → a VM apanha no pull seguinte. **Nada depende do Mac estar ligado.**

**Regra de ouro:** sempre `--ff-only`; se não for fast-forward, parar e reportar.

---

## 6. Instruções rápidas para os Tivs

### Para todos:
1. Ler este `00_INDEX.md` pelo conector GitHub (`get_file_contents`, `owner="Altars-Group"`, `repo="ellocene-ops"`).
2. Ler o índice da tua área pelo mesmo conector.
3. Processos/registos → conector Fibery.
4. Só depois agir. Se o conector falhar, reportar com o erro cru (não improvisar de memória).

### Para o Credo (quando estiver no Mac):
1. Se quiser atualizar a base, `cd /workspace/ellocene-ops` e faça commits normais.
2. O DevOps cuida do sync automático.

### Para o DevOps:
1. O repo está clonado em `/workspace/ellocene-ops` (leitura de emergência; o canal canónico é o MCP).
2. Deploy key: **fora do caminho crítico** (P3). O registo falha com HTTP 422 «Deploy keys are disabled for this repository» — bloqueio da org, não do token. Só se reabre quando um trabalho exigir mesmo a VM.
3. Serviço de sync: `ellocene-sync.timer` — travado pela guarda `RECONCILIACAO-PENDENTE` até reconciliação manual.

---

**Prova de funcionamento:**
- `git rev-parse --abbrev-ref HEAD` → `main`
- `ls -d 0*_*` → as 7 pastas principais
- `git log --oneline -2` → os 2 commits recentes
- `test -f 00_INDEX.md && echo OK` → `OK`

---

**NOTA DE SISTEMA:** Este é o primeiro documento que, em vez de anúncio, tem o conteúdo real. É a prova de que a base canónica está operacional — mesmo que o Fibery não esteja a funcionar corretamente.