---
task: "Carryover"
responsavel: "@planos"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - tarefas não fechadas
Saida: |
  - lista de acções para próximo plano
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *carryover

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@planos
*carryover
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tarefas não fechadas` | string | Yes | tarefas não fechadas |

## Output

- **lista de acções para próximo plano**: lista de acções para próximo plano

## Origin

Confidence: 91%
