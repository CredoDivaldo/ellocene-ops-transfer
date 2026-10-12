---
task: "Relatorio Holding"
responsavel: "@relatorios"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - período
Saida: |
  - conteúdo Estado da Holding (filhas + projetos + KPIs + reuniões + tarefas) → @docs PDF
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *relatorio-holding

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@relatorios
*relatorio-holding
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `período` | string | Yes | período |

## Output

- **conteúdo Estado da Holding (filhas + projetos + KPIs + reuniões + tarefas) → @docs PDF**: conteúdo Estado da Holding (filhas + projetos + KPIs + reuniões + tarefas) → @docs PDF

## Origin

Confidence: 92%
