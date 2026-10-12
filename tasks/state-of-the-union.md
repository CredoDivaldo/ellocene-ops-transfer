---
task: "State Of The Union"
responsavel: "@relatorios"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - período + dados de todos os agentes
Saida: |
  - relatório unificado executivo → @docs PDF
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *state-of-the-union

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@relatorios
*state-of-the-union
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `período + dados de todos os agentes` | string | Yes | período + dados de todos os agentes |

## Output

- **relatório unificado executivo → @docs PDF**: relatório unificado executivo → @docs PDF

## Origin

Confidence: 90%
