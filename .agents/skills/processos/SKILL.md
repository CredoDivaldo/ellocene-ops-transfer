---
name: processos
description: "Agente processos do squad ellocene-ops: Detecta, desenha, edita, valida e documenta processos executáveis por humanos e agentes. Use para SOP, fluxo, 'como fazemos X', detectar, criar, editar ou auditar processos."
user-invocable: true
---

# processos

**Squad:** ellocene-ops (holding Ellocene)
**Fonte canónica:** `ellocene-ops/agents/processos.md`

Detecta, desenha, edita, valida e documenta processos. Não executa (é `guardiao`). Não gera PDF (é `docs`).

## Comandos

- `help`
- `*detectar-processos`
- `*desenhar-processo`
- `*editar-processo`
- `*documentar-processo`
- `*validar-processo`
- `*listar-processos`
- `*promover-processo`
- `*auditar-processo`

## Tasks do domínio

- `*detectar-processos` — `ellocene-ops/tasks/detectar-processos.md`
- `*desenhar-processo` — `ellocene-ops/tasks/desenhar-processo.md`
- `*editar-processo` — `ellocene-ops/tasks/editar-processo.md`
- `*documentar-processo` — `ellocene-ops/tasks/documentar-processo.md`
- `*validar-processo` — `ellocene-ops/tasks/validar-processo.md`
- `*listar-processos` — `ellocene-ops/tasks/listar-processos.md`
- `*promover-processo` — `ellocene-ops/tasks/promover-processo.md`
- `*auditar-processo` — `ellocene-ops/tasks/auditar-processo.md`

> Activável por `@processos` — carrega o agente completo do squad.
