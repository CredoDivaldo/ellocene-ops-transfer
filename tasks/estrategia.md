---
task: "Estrategia"
responsavel: "@ceo"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - contexto (estado da holding/filhas) + pergunta
Saida: |
  - análise estratégica + próximos passos prioritários
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *estrategia

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@ceo
*estrategia
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `contexto (estado da holding/filhas) + pergunta` | string | Yes | contexto (estado da holding/filhas) + pergunta |

## Output

- **análise estratégica + próximos passos prioritários**: análise estratégica + próximos passos prioritários

## Origin

Confidence: 89%
