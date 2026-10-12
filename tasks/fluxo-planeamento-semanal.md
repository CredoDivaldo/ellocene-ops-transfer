---
task: "Fluxo Planeamento Semanal"
responsavel: "@guardiao"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - semana
Saida: |
  - cadeia: @actas (tarefas) + @registo (carryover) + @kpis (metas) → @planos (gerar-planos-semana) → gate Credo → publicação Fibery → @relatorios (estado de execução)
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *fluxo-planeamento-semanal

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@guardiao
*fluxo-planeamento-semanal
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `semana` | string | Yes | semana |

## Output

- **cadeia: @actas (tarefas) + @registo (carryover) + @kpis (metas) → @planos (gerar-planos-semana) → gate Credo → publicação Fibery → @relatorios (estado de execução)**: cadeia: @actas (tarefas) + @registo (carryover) + @kpis (metas) → @planos (gerar-planos-semana) → gate Credo → publicação Fibery → @relatorios (estado de execução)

## Origin

Confidence: 92%
