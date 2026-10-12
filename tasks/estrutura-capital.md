---
task: "Estrutura Capital"
responsavel: "@cfo"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - estado actual + objectivo
Saida: |
  - opções de estrutura de capital + fluxo de caixa + risco
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *estrutura-capital

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@cfo
*estrutura-capital
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `estado actual + objectivo` | string | Yes | estado actual + objectivo |

## Output

- **opções de estrutura de capital + fluxo de caixa + risco**: opções de estrutura de capital + fluxo de caixa + risco

## Origin

Confidence: 87%
