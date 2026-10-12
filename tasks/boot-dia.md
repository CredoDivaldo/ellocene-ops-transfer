---
task: "Boot Dia"
responsavel: "@planos"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - plano semanal + dia actual
Saida: |
  - plano diário com time blocking + guardrails + check-in
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *boot-dia

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@planos
*boot-dia
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `plano semanal + dia actual` | string | Yes | plano semanal + dia actual |

## Output

- **plano diário com time blocking + guardrails + check-in**: plano diário com time blocking + guardrails + check-in

## Origin

Confidence: 95%
