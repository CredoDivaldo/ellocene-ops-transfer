---
task: "Pipelines"
responsavel: "@cro"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - estado pipeline (Ellocene/Client + Project)
Saida: |
  - análise de pipeline + acções para fechar
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *pipelines

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@cro
*pipelines
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `estado pipeline (Ellocene/Client + Project)` | string | Yes | estado pipeline (Ellocene/Client + Project) |

## Output

- **análise de pipeline + acções para fechar**: análise de pipeline + acções para fechar

## Origin

Confidence: 89%
