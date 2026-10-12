---
task: "Auditar Fibery"
responsavel: "@governanca"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - base opcional
Saida: |
  - relatório: relações em falta, campos vazios, entidades desligadas
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *auditar-fibery

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@governanca
*auditar-fibery
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `base opcional` | string | Yes | base opcional |

## Output

- **relatório: relações em falta, campos vazios, entidades desligadas**: relatório: relações em falta, campos vazios, entidades desligadas

## Origin

Confidence: 90%
