---
task: "Pricing"
responsavel: "@cro"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - produto/serviço + mercado
Saida: |
  - recomendação de pricing baseado em valor
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *pricing

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@cro
*pricing
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `produto/serviço + mercado` | string | Yes | produto/serviço + mercado |

## Output

- **recomendação de pricing baseado em valor**: recomendação de pricing baseado em valor

## Origin

Confidence: 87%
