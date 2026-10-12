---
task: "Validar Relacoes"
responsavel: "@governanca"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - entidades suspeitas
Saida: |
  - proposta → aprovação → correcções aplicadas
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *validar-relacoes

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@governanca
*validar-relacoes
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `entidades suspeitas` | string | Yes | entidades suspeitas |

## Output

- **proposta → aprovação → correcções aplicadas**: proposta → aprovação → correcções aplicadas

## Origin

Confidence: 88%
