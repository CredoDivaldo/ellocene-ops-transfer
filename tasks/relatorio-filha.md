---
task: "Relatorio Filha"
responsavel: "@relatorios"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - filha + período
Saida: |
  - conteúdo por filha (projectos, KPIs, movimentos, reuniões) → @docs PDF
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *relatorio-filha

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@relatorios
*relatorio-filha
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `filha + período` | string | Yes | filha + período |

## Output

- **conteúdo por filha (projectos, KPIs, movimentos, reuniões) → @docs PDF**: conteúdo por filha (projectos, KPIs, movimentos, reuniões) → @docs PDF

## Origin

Confidence: 91%
