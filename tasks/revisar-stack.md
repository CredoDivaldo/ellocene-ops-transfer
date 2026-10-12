---
task: "Revisar Stack"
responsavel: "@cto"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - stack actual
Saida: |
  - análise + melhorias sugeridas
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *revisar-stack

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@cto
*revisar-stack
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `stack actual` | string | Yes | stack actual |

## Output

- **análise + melhorias sugeridas**: análise + melhorias sugeridas

## Origin

Confidence: 88%
