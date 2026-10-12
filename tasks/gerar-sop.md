---
task: "Gerar Sop"
responsavel: "@docs"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - processo + passos + responsáveis + identidade
Saida: |
  - HTML → PDF WeasyPrint → Drive + Fibery Document (Tipo: Runbook)
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *gerar-sop

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@docs
*gerar-sop
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `processo + passos + responsáveis + identidade` | string | Yes | processo + passos + responsáveis + identidade |

## Output

- **HTML → PDF WeasyPrint → Drive + Fibery Document (Tipo: Runbook)**: HTML → PDF WeasyPrint → Drive + Fibery Document (Tipo: Runbook)

## Origin

Confidence: 92%
