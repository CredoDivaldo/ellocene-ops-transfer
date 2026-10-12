---
task: "Checkout"
responsavel: "@planos"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - estado final do dia
Saida: |
  - KPIs diários + primeira acção de amanhã + carryover
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *checkout

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@planos
*checkout
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `estado final do dia` | string | Yes | estado final do dia |

## Output

- **KPIs diários + primeira acção de amanhã + carryover**: KPIs diários + primeira acção de amanhã + carryover

## Origin

Confidence: 93%
