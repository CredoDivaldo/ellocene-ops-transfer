---
task: "Estado Portfolio"
responsavel: "@portfolio"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - nenhum
Saida: |
  - matriz: filhas por estado, sector, % holding, projectos, KPIs ativos
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *estado-portfolio

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@portfolio
*estado-portfolio
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `nenhum` | string | Yes | nenhum |

## Output

- **matriz: filhas por estado, sector, % holding, projectos, KPIs ativos**: matriz: filhas por estado, sector, % holding, projectos, KPIs ativos

## Origin

Confidence: 94%
