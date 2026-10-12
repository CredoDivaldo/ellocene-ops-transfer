---
task: "Gerar Acta Projecto"
responsavel: "@actas"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - transcrição reunião de projecto
Saida: |
  - acta de projecto + tarefas → @planos
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *gerar-acta-projecto

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@actas
*gerar-acta-projecto
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `transcrição reunião de projecto` | string | Yes | transcrição reunião de projecto |

## Output

- **acta de projecto + tarefas → @planos**: acta de projecto + tarefas → @planos

## Origin

Confidence: 94%
