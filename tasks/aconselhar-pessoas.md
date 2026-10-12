---
task: "Aconselhar Pessoas"
responsavel: "@chro"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - pergunta de pessoas/cultura do Credo
Saida: |
  - recomendação + fontes
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *aconselhar-pessoas

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@chro
*aconselhar-pessoas
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pergunta de pessoas/cultura do Credo` | string | Yes | pergunta de pessoas/cultura do Credo |

## Output

- **recomendação + fontes**: recomendação + fontes

## Origin

Confidence: 88%
