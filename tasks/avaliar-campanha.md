---
task: "Avaliar Campanha"
responsavel: "@cmo"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - campanha/peças + resultados
Saida: |
  - avaliação + recomendações de optimização
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *avaliar-campanha

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@cmo
*avaliar-campanha
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `campanha/peças + resultados` | string | Yes | campanha/peças + resultados |

## Output

- **avaliação + recomendações de optimização**: avaliação + recomendações de optimização

## Origin

Confidence: 89%
