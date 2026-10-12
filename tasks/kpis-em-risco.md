---
task: "Kpis Em Risco"
responsavel: "@kpis"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - nenhum
Saida: |
  - KPIs Activo com valor além do limiar/direcção → Em Risco + alerta
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *kpis-em-risco

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@kpis
*kpis-em-risco
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `nenhum` | string | Yes | nenhum |

## Output

- **KPIs Activo com valor além do limiar/direcção → Em Risco + alerta**: KPIs Activo com valor além do limiar/direcção → Em Risco + alerta

## Origin

Confidence: 93%
