---
task: "Fluxo Completo Reuniao"
responsavel: "@guardiao"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - transcrição .txt de reunião
Saida: |
  - cadeia: @actas → gate → @docs(se acta formal) → @planos tarefas
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *fluxo-completo-reuniao

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@guardiao
*fluxo-completo-reuniao
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `transcrição .txt de reunião` | string | Yes | transcrição .txt de reunião |

## Output

- **cadeia: @actas → gate → @docs(se acta formal) → @planos tarefas**: cadeia: @actas → gate → @docs(se acta formal) → @planos tarefas

## Origin

Confidence: 93%
