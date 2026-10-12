---
task: "Orcamento Grupo"
responsavel: "@cfo"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - período + metas
Saida: |
  - orçamento proposto de grupo + premissas
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *orcamento-grupo

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@cfo
*orcamento-grupo
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `período + metas` | string | Yes | período + metas |

## Output

- **orçamento proposto de grupo + premissas**: orçamento proposto de grupo + premissas

## Origin

Confidence: 88%
