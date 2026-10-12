---
task: "Pesquisar Legislacao"
responsavel: "@legal"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - tema jurídico
Saida: |
  - resumo da legislação aplicável com fontes
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *pesquisar-legislacao

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@legal
*pesquisar-legislacao
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tema jurídico` | string | Yes | tema jurídico |

## Output

- **resumo da legislação aplicável com fontes**: resumo da legislação aplicável com fontes

## Origin

Confidence: 90%
