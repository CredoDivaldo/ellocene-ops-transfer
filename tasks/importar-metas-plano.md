---
task: "Importar Metas Plano"
responsavel: "@kpis"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - plano de negócio/metas por período
Saida: |
  - KPIs propostos para criação a partir do plano
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *importar-metas-plano

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@kpis
*importar-metas-plano
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `plano de negócio/metas por período` | string | Yes | plano de negócio/metas por período |

## Output

- **KPIs propostos para criação a partir do plano**: KPIs propostos para criação a partir do plano

## Origin

Confidence: 88%
