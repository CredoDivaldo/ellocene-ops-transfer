---
task: "Listar Kpis"
responsavel: "@kpis"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - filtros (categoria, estado, filha)
Saida: |
  - lista de KPIs com estado
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *listar-kpis

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@kpis
*listar-kpis
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `filtros (categoria, estado, filha)` | string | Yes | filtros (categoria, estado, filha) |

## Output

- **lista de KPIs com estado**: lista de KPIs com estado

## Origin

Confidence: 95%
