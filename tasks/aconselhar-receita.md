---
task: "Aconselhar Receita"
responsavel: "@cro"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - pergunta de vendas/receita do Credo
Saida: |
  - recomendação + fontes
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *aconselhar-receita

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@cro
*aconselhar-receita
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pergunta de vendas/receita do Credo` | string | Yes | pergunta de vendas/receita do Credo |

## Output

- **recomendação + fontes**: recomendação + fontes

## Origin

Confidence: 89%
