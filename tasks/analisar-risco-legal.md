---
task: "Analisar Risco Legal"
responsavel: "@legal"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - contrato/documento/obrigação
Saida: |
  - análise de risco jurídico + recomendações
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *analisar-risco-legal

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@legal
*analisar-risco-legal
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contrato/documento/obrigação` | string | Yes | contrato/documento/obrigação |

## Output

- **análise de risco jurídico + recomendações**: análise de risco jurídico + recomendações

## Origin

Confidence: 87%
