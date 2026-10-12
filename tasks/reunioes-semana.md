---
task: "Reunioes Semana"
responsavel: "@planos"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - semana
Saida: |
  - agenda semanal de reuniões + actas em falta
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *reunioes-semana

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@planos
*reunioes-semana
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `semana` | string | Yes | semana |

## Output

- **agenda semanal de reuniões + actas em falta**: agenda semanal de reuniões + actas em falta

## Origin

Confidence: 93%
