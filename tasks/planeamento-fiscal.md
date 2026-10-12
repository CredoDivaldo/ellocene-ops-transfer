---
task: "Planeamento Fiscal"
responsavel: "@cfo"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - movimentos + filhas
Saida: |
  - análise de eficiência fiscal dentro da lei → @legal valida
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *planeamento-fiscal

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@cfo
*planeamento-fiscal
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `movimentos + filhas` | string | Yes | movimentos + filhas |

## Output

- **análise de eficiência fiscal dentro da lei → @legal valida**: análise de eficiência fiscal dentro da lei → @legal valida

## Origin

Confidence: 85%
