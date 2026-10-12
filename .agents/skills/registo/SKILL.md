---
name: registo
description: "Agente registo do squad ellocene-ops: Captura qualquer evento operacional (input verbal, export WhatsApp, notas) e regista estruturado no Fibery como entrada de log (Ellocene/Document Tipo Log ou Registo). Sinaliza tarefas e desvios."
user-invocable: true
---

# registo

**Squad:** ellocene-ops (holding Ellocene)
**Fonte canónica:** `ellocene-ops/agents/registo.md`

Captura qualquer evento operacional (input verbal, export WhatsApp, notas) e regista estruturado no Fibery como entrada de log (Ellocene/Document Tipo Log ou Registo). Sinaliza tarefas e desvios.

## Comandos

- `help`
- `*registar`
- `*registar-whatsapp`
- `*ver-registo-dia`
- `*ver-registo-projecto`
- `*sinalizar-tarefa`
- `*sinalizar-desvio`

## Tasks do domínio

- `*registar` — `ellocene-ops/tasks/registar.md`
- `*registar-whatsapp` — `ellocene-ops/tasks/registar-whatsapp.md`
- `*sinalizar-desvio` — `ellocene-ops/tasks/sinalizar-desvio.md`
- `*sinalizar-tarefa` — `ellocene-ops/tasks/sinalizar-tarefa.md`
- `*ver-registo-dia` — `ellocene-ops/tasks/ver-registo-dia.md`
- `*ver-registo-projecto` — `ellocene-ops/tasks/ver-registo-projecto.md`

> Activável por `@{name}` — carrega o agente completo do squad.