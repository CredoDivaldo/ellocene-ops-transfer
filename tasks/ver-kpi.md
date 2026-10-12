---
task: "Ver Kpi"
responsavel: "@kpis"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - kpi ou filha
Saida: |
  - ficha: meta, actual, direcção, histórico do log, estado
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *ver-kpi

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@kpis
*ver-kpi
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `kpi ou filha` | string | Yes | kpi ou filha |

## Output

- **ficha: meta, actual, direcção, histórico do log, estado**: ficha: meta, actual, direcção, histórico do log, estado

## Origin

Confidence: 96%
