---
task: "Minuta Deliberacao"
responsavel: "@legal"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - decisão dos sócios + tipo (maioria/2-3/unanimidade)
Saida: |
  - minuta de deliberação social formal conforme tipo de decisão
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *minuta-deliberacao

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@legal
*minuta-deliberacao
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `decisão dos sócios + tipo (maioria/2-3/unanimidade)` | string | Yes | decisão dos sócios + tipo (maioria/2-3/unanimidade) |

## Output

- **minuta de deliberação social formal conforme tipo de decisão**: minuta de deliberação social formal conforme tipo de decisão

## Origin

Confidence: 89%
