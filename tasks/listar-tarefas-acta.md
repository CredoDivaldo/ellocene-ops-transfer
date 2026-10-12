---
task: "Listar Tarefas Acta"
responsavel: "@actas"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - acta gerada
Saida: |
  - lista estruturada de tarefas → handoff @planos
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *listar-tarefas-acta

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@actas
*listar-tarefas-acta
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `acta gerada` | string | Yes | acta gerada |

## Output

- **lista estruturada de tarefas → handoff @planos**: lista estruturada de tarefas → handoff @planos

## Origin

Confidence: 95%
