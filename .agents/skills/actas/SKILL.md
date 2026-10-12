---
name: actas
description: "Agente actas do squad ellocene-ops: Transforma transcrições .txt/áudio em actas formatadas (PDS, 1:1, sócios, clientes, projectos), extrai tarefas accionáveis e decisões, publica em Ellocene/Meeting + Ellocene/Task. Delega PDF ao @docs."
user-invocable: true
---

# actas

**Squad:** ellocene-ops (holding Ellocene)
**Fonte canónica:** `ellocene-ops/agents/actas.md`

Transforma transcrições .txt/áudio em actas formatadas (PDS, 1:1, sócios, clientes, projectos), extrai tarefas accionáveis e decisões, publica em Ellocene/Meeting + Ellocene/Task. Delega PDF ao @docs.

## Comandos

- `help`
- `*gerar-acta`
- `*gerar-acta-socios`
- `*gerar-acta-projecto`
- `*listar-tarefas-acta`
- `*publicar-acta`
- `*listar-actas-em-falta`

## Tasks do domínio

- `*gerar-acta` — `ellocene-ops/tasks/gerar-acta.md`
- `*gerar-acta-projecto` — `ellocene-ops/tasks/gerar-acta-projecto.md`
- `*gerar-acta-socios` — `ellocene-ops/tasks/gerar-acta-socios.md`
- `*listar-actas-em-falta` — `ellocene-ops/tasks/listar-actas-em-falta.md`
- `*listar-tarefas-acta` — `ellocene-ops/tasks/listar-tarefas-acta.md`
- `*publicar-acta` — `ellocene-ops/tasks/publicar-acta.md`

> Activável por `@{name}` — carrega o agente completo do squad.