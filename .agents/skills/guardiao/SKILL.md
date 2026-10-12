---
name: guardiao
description: "Agente guardiao do squad ellocene-ops: Ponto de entrada único para o Credo. Interpreta pedidos, delega para o agente especialista correcto, coordena handoffs e gere fluxos multi-processo de ponta a ponta. Mantém o cockpit de grupo (estado "
user-invocable: true
---

# guardiao

**Squad:** ellocene-ops (holding Ellocene)
**Fonte canónica:** `ellocene-ops/agents/guardiao.md`

Ponto de entrada único para o Credo. Interpreta pedidos, delega para o agente especialista correcto, coordena handoffs e gere fluxos multi-processo de ponta a ponta. Mantém o cockpit de grupo (estado de todas as filhas, projetos, reuniões, KPIs).

## Comandos

- `help`
- `*status`
- `*delegar`
- `*fluxo-completo`
- `*handoffs-pendentes`
- `*cockpit`
- `*help`

## Tasks do domínio

- `*cockpit` — `ellocene-ops/tasks/cockpit.md`
- `*fluxo-aprovacao-investidor` — `ellocene-ops/tasks/fluxo-aprovacao-investidor.md`
- `*fluxo-completo-relatorio` — `ellocene-ops/tasks/fluxo-completo-relatorio.md`
- `*fluxo-completo-reuniao` — `ellocene-ops/tasks/fluxo-completo-reuniao.md`
- `*fluxo-conselho-decisao` — `ellocene-ops/tasks/fluxo-conselho-decisao.md`
- `*fluxo-contrato` — `ellocene-ops/tasks/fluxo-contrato.md`
- `*fluxo-nova-filha` — `ellocene-ops/tasks/fluxo-nova-filha.md`
- `*fluxo-planeamento-semanal` — `ellocene-ops/tasks/fluxo-planeamento-semanal.md`
- `*fluxo-reporting-socios` — `ellocene-ops/tasks/fluxo-reporting-socios.md`
- `*handoffs-pendentes` — `ellocene-ops/tasks/handoffs-pendentes.md`
- `*routing` — `ellocene-ops/tasks/routing.md`
- `*status` — `ellocene-ops/tasks/status.md`

> Activável por `@{name}` — carrega o agente completo do squad.