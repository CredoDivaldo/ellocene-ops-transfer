---
task: "Metricas Saude"
responsavel: "@cfo"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - dados financeiros (Fibery Ellocene/Financeiro)
Saida: |
  - leitura da saúde financeira + alertas
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *metricas-saude

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@cfo
*metricas-saude
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `dados financeiros (Fibery Ellocene/Financeiro)` | string | Yes | dados financeiros (Fibery Ellocene/Financeiro) |

## Output

- **leitura da saúde financeira + alertas**: leitura da saúde financeira + alertas

## Origin

Confidence: 90%
