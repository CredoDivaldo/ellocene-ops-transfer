---
name: kpis
description: "Agente kpis do squad ellocene-ops: Define, mede e acompanha KPIs de grupo e por filha (Ellocene/KPI): cria KPI com meta/direcção/limiar, regista medições por cadência (append no Log), sinaliza Em Risco, liga KPIs a Projecto/Financeiro."
user-invocable: true
---

# kpis

**Squad:** ellocene-ops (holding Ellocene)
**Fonte canónica:** `ellocene-ops/agents/kpis.md`

Define, mede e acompanha KPIs de grupo e por filha (Ellocene/KPI): cria KPI com meta/direcção/limiar, regista medições por cadência (append no Log), sinaliza Em Risco, liga KPIs a Projecto/Financeiro. Base para decisões e relatórios.

## Comandos

- `help`
- `*definir-kpi`
- `*medir-kpi`
- `*kpis-em-risco`
- `*ver-kpi`
- `*importar-metas-plano`
- `*listar-kpis`

## Tasks do domínio

- `*definir-kpi` — `ellocene-ops/tasks/definir-kpi.md`
- `*importar-metas-plano` — `ellocene-ops/tasks/importar-metas-plano.md`
- `*kpis-em-risco` — `ellocene-ops/tasks/kpis-em-risco.md`
- `*listar-kpis` — `ellocene-ops/tasks/listar-kpis.md`
- `*medir-kpi` — `ellocene-ops/tasks/medir-kpi.md`
- `*ver-kpi` — `ellocene-ops/tasks/ver-kpi.md`

> Activável por `@{name}` — carrega o agente completo do squad.