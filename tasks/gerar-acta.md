---
task: "Gerar Acta"
responsavel: "@actas"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - ficheiro .txt/transcrição + tipo de reunião
Saida: |
  - acta formatada + lista de decisões + tarefas
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *gerar-acta

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@actas
*gerar-acta
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `ficheiro .txt/transcrição + tipo de reunião` | string | Yes | ficheiro .txt/transcrição + tipo de reunião |

## Output

- **acta formatada + lista de decisões + tarefas**: acta formatada + lista de decisões + tarefas

## Origin

Confidence: 95%
