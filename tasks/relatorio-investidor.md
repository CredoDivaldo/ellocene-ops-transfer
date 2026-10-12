---
task: "Relatorio Investidor"
responsavel: "@relatorios"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - período
Saida: |
  - conteúdo para investidor (SCP Jericó): financeiro de filhas + KPIs + riscos → @docs PDF
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *relatorio-investidor

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@relatorios
*relatorio-investidor
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `período` | string | Yes | período |

## Output

- **conteúdo para investidor (SCP Jericó): financeiro de filhas + KPIs + riscos → @docs PDF**: conteúdo para investidor (SCP Jericó): financeiro de filhas + KPIs + riscos → @docs PDF

## Origin

Confidence: 89%
