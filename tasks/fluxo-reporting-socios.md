---
task: "Fluxo Reporting Socios"
responsavel: "@guardiao"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - período
Saida: |
  - cadeia: dados de todos os agentes operacionais → @relatorios (Estado da Holding) → @ceo (leitura estratégica) → @docs (PDF identidade holding) → @governanca (envio a sócios + registro)
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *fluxo-reporting-socios

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@guardiao
*fluxo-reporting-socios
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `período` | string | Yes | período |

## Output

- **cadeia: dados de todos os agentes operacionais → @relatorios (Estado da Holding) → @ceo (leitura estratégica) → @docs (PDF identidade holding) → @governanca (envio a sócios + registro)**: cadeia: dados de todos os agentes operacionais → @relatorios (Estado da Holding) → @ceo (leitura estratégica) → @docs (PDF identidade holding) → @governanca (envio a sócios + registro)

## Origin

Confidence: 90%
