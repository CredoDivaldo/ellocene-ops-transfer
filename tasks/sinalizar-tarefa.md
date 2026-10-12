---
task: "Sinalizar Tarefa"
responsavel: "@registo"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - evento que gera tarefa
Saida: |
  - proposta de tarefa Ellocene/Task → @planos/@guardiao
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *sinalizar-tarefa

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@registo
*sinalizar-tarefa
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `evento que gera tarefa` | string | Yes | evento que gera tarefa |

## Output

- **proposta de tarefa Ellocene/Task → @planos/@guardiao**: proposta de tarefa Ellocene/Task → @planos/@guardiao

## Origin

Confidence: 91%
