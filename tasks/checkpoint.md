---
task: "Checkpoint"
responsavel: "@planos"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - estado actual das tarefas
Saida: |
  - avaliação de progresso, desvios, ajustes
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *checkpoint

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@planos
*checkpoint
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `estado actual das tarefas` | string | Yes | estado actual das tarefas |

## Output

- **avaliação de progresso, desvios, ajustes**: avaliação de progresso, desvios, ajustes

## Origin

Confidence: 94%
