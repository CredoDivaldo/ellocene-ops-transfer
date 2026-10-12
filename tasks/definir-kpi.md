---
task: "Definir Kpi"
responsavel: "@kpis"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - nome + meta + unidade + direcção + cadência + owner + limiar
Saida: |
  - entidade Ellocene/KPI criada → gate Credo
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *definir-kpi

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@kpis
*definir-kpi
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `nome + meta + unidade + direcção + cadência + owner + limiar` | string | Yes | nome + meta + unidade + direcção + cadência + owner + limiar |

## Output

- **entidade Ellocene/KPI criada → gate Credo**: entidade Ellocene/KPI criada → gate Credo

## Origin

Confidence: 93%
