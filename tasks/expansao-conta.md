---
task: "Expansao Conta"
responsavel: "@cro"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - cliente existente
Saida: |
  - plano de expansão (upsell/cross-sell)
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *expansao-conta

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@cro
*expansao-conta
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `cliente existente` | string | Yes | cliente existente |

## Output

- **plano de expansão (upsell/cross-sell)**: plano de expansão (upsell/cross-sell)

## Origin

Confidence: 87%
