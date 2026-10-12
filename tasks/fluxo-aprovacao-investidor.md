---
task: "Fluxo Aprovacao Investidor"
responsavel: "@guardiao"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - necessidade do investidor SCP (Jericó)
Saida: |
  - cadeia: @cfo (relatório financeiro) + @kpis (resultados) + @ceo (narrativa) → @relatorios (relatorio-investidor) → @legal (conformidade SCP) → gate Credo → @docs (PDF) → envio
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *fluxo-aprovacao-investidor

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@guardiao
*fluxo-aprovacao-investidor
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `necessidade do investidor SCP (Jericó)` | string | Yes | necessidade do investidor SCP (Jericó) |

## Output

- **cadeia: @cfo (relatório financeiro) + @kpis (resultados) + @ceo (narrativa) → @relatorios (relatorio-investidor) → @legal (conformidade SCP) → gate Credo → @docs (PDF) → envio**: cadeia: @cfo (relatório financeiro) + @kpis (resultados) + @ceo (narrativa) → @relatorios (relatorio-investidor) → @legal (conformidade SCP) → gate Credo → @docs (PDF) → envio

## Origin

Confidence: 86%
