---
task: "Sinalizar Desvio"
responsavel: "@registo"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - evento que altera plano
Saida: |
  - alerta ao Credo com impacto e sugestão
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *sinalizar-desvio

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@registo
*sinalizar-desvio
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `evento que altera plano` | string | Yes | evento que altera plano |

## Output

- **alerta ao Credo com impacto e sugestão**: alerta ao Credo com impacto e sugestão

## Origin

Confidence: 90%
