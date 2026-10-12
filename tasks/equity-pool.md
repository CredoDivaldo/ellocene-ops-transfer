---
task: "Equity Pool"
responsavel: "@chro"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - filha + fase + equipa
Saida: |
  - proposta de equity pool compatível com holding → @legal valida
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *equity-pool

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@chro
*equity-pool
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `filha + fase + equipa` | string | Yes | filha + fase + equipa |

## Output

- **proposta de equity pool compatível com holding → @legal valida**: proposta de equity pool compatível com holding → @legal valida

## Origin

Confidence: 84%
