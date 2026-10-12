---
task: "Listar Actas Em Falta"
responsavel: "@actas"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - período
Saida: |
  - reuniões com estado 'Acta em Falta' → lembretes
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *listar-actas-em-falta

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@actas
*listar-actas-em-falta
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `período` | string | Yes | período |

## Output

- **reuniões com estado 'Acta em Falta' → lembretes**: reuniões com estado 'Acta em Falta' → lembretes

## Origin

Confidence: 92%
