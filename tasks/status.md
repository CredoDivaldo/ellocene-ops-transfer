---
task: "Status"
responsavel: "@guardiao"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - filtro opcional (agente, processo, filha, período)
Saida: |
  - dashboard: handoffs pendentes, gates, processos em curso
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *status

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@guardiao
*status
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `filtro opcional (agente, processo, filha, período)` | string | Yes | filtro opcional (agente, processo, filha, período) |

## Output

- **dashboard: handoffs pendentes, gates, processos em curso**: dashboard: handoffs pendentes, gates, processos em curso

## Origin

Confidence: 94%
