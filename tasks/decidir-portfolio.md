---
task: "Decidir Portfolio"
responsavel: "@ceo"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - oportunidade/estado portfólio
Saida: |
  - recomendação de decisão de portfólio (criar/financiar/vender/fechar) + racional
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *decidir-portfolio

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@ceo
*decidir-portfolio
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `oportunidade/estado portfólio` | string | Yes | oportunidade/estado portfólio |

## Output

- **recomendação de decisão de portfólio (criar/financiar/vender/fechar) + racional**: recomendação de decisão de portfólio (criar/financiar/vender/fechar) + racional

## Origin

Confidence: 88%
