---
task: "Medir Kpi"
responsavel: "@kpis"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - kpi(s) + medição + data
Saida: |
  - Valor Actual actualizado + append no Log + estado
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *medir-kpi

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@kpis
*medir-kpi
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `kpi(s) + medição + data` | string | Yes | kpi(s) + medição + data |

## Output

- **Valor Actual actualizado + append no Log + estado**: Valor Actual actualizado + append no Log + estado

## Origin

Confidence: 95%
