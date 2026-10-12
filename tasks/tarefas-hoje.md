---
task: "Tarefas Hoje"
responsavel: "@planos"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - data
Saida: |
  - tarefas de hoje (Fibery/Task) + reuniões do dia + foco proposto
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *tarefas-hoje

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@planos
*tarefas-hoje
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `data` | string | Yes | data |

## Output

- **tarefas de hoje (Fibery/Task) + reuniões do dia + foco proposto**: tarefas de hoje (Fibery/Task) + reuniões do dia + foco proposto

## Origin

Confidence: 95%
