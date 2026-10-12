---
task: "Publicar Acta"
responsavel: "@actas"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - acta aprovada
Saida: |
  - entidade Ellocene/Meeting actualizada ou criada + Acta doc + workflow
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *publicar-acta

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@actas
*publicar-acta
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `acta aprovada` | string | Yes | acta aprovada |

## Output

- **entidade Ellocene/Meeting actualizada ou criada + Acta doc + workflow**: entidade Ellocene/Meeting actualizada ou criada + Acta doc + workflow

## Origin

Confidence: 94%
