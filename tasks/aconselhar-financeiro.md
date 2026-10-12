---
task: "Aconselhar Financeiro"
responsavel: "@cfo"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - pergunta financeira do Credo
Saida: |
  - conselho com racional + fontes
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *aconselhar-financeiro

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@cfo
*aconselhar-financeiro
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pergunta financeira do Credo` | string | Yes | pergunta financeira do Credo |

## Output

- **conselho com racional + fontes**: conselho com racional + fontes

## Origin

Confidence: 89%
