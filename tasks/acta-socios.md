---
task: "Acta Socios"
responsavel: "@governanca"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - transcrição/reunião de sócios
Saida: |
  - minuta de acta de reunião de sócios → gate sócios → @actas para acta formal/PDF
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *acta-socios

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@governanca
*acta-socios
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `transcrição/reunião de sócios` | string | Yes | transcrição/reunião de sócios |

## Output

- **minuta de acta de reunião de sócios → gate sócios → @actas para acta formal/PDF**: minuta de acta de reunião de sócios → gate sócios → @actas para acta formal/PDF

## Origin

Confidence: 90%
