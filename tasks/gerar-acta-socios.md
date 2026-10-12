---
task: "Gerar Acta Socios"
responsavel: "@actas"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - transcrição reunião de sócios
Saida: |
  - acta formal de sócios (template específico) + handoff @docs PDF
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *gerar-acta-socios

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@actas
*gerar-acta-socios
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `transcrição reunião de sócios` | string | Yes | transcrição reunião de sócios |

## Output

- **acta formal de sócios (template específico) + handoff @docs PDF**: acta formal de sócios (template específico) + handoff @docs PDF

## Origin

Confidence: 93%
