---
task: "Fluxo Completo Relatorio"
responsavel: "@guardiao"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - tipo de relatório + período
Saida: |
  - cadeia: @registo+@planos+@kpis+@portfolio dados → @relatorios conteúdo → @docs PDF → @governanca valida
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *fluxo-completo-relatorio

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@guardiao
*fluxo-completo-relatorio
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tipo de relatório + período` | string | Yes | tipo de relatório + período |

## Output

- **cadeia: @registo+@planos+@kpis+@portfolio dados → @relatorios conteúdo → @docs PDF → @governanca valida**: cadeia: @registo+@planos+@kpis+@portfolio dados → @relatorios conteúdo → @docs PDF → @governanca valida

## Origin

Confidence: 91%
