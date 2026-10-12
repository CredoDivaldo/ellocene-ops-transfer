---
name: planos
description: "Agente planos do squad ellocene-ops: Gera planos semanais (por filha/projecto), opera cockpit diário com checkpoints e carryover, sinaliza reuniões em falta e tarefas por começar no Fibery (Ellocene/Task), coordena time blocking no calen"
user-invocable: true
---

# planos

**Squad:** ellocene-ops (holding Ellocene)
**Fonte canónica:** `ellocene-ops/agents/planos.md`

Gera planos semanais (por filha/projecto), opera cockpit diário com checkpoints e carryover, sinaliza reuniões em falta e tarefas por começar no Fibery (Ellocene/Task), coordena time blocking no calendário do operador.

## Comandos

- `help`
- `*gerar-planos-semana`
- `*boot-dia`
- `*checkpoint`
- `*checkout`
- `*carryover`
- `*tarefas-hoje`
- `*reunioes-semana`

## Tasks do domínio

- `*boot-dia` — `ellocene-ops/tasks/boot-dia.md`
- `*carryover` — `ellocene-ops/tasks/carryover.md`
- `*checkout` — `ellocene-ops/tasks/checkout.md`
- `*checkpoint` — `ellocene-ops/tasks/checkpoint.md`
- `*gerar-planos-semana` — `ellocene-ops/tasks/gerar-planos-semana.md`
- `*reunioes-semana` — `ellocene-ops/tasks/reunioes-semana.md`
- `*tarefas-hoje` — `ellocene-ops/tasks/tarefas-hoje.md`

> Activável por `@{name}` — carrega o agente completo do squad.