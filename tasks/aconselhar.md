---
task: "Aconselhar"
responsavel: "@ceo"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - pedido de conselho/estratégia do Credo
Saida: |
  - recomendação com fundamentação (fontes pesquisadas) + opções + prós/contras
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *aconselhar

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@ceo
*aconselhar
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pedido de conselho/estratégia do Credo` | string | Yes | pedido de conselho/estratégia do Credo |

## Output

- **recomendação com fundamentação (fontes pesquisadas) + opções + prós/contras**: recomendação com fundamentação (fontes pesquisadas) + opções + prós/contras

## Origin

Confidence: 90%
