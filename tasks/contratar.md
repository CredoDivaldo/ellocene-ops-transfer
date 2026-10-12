---
task: "Contratar"
responsavel: "@chro"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - função + requisitos + orçamento
Saida: |
  - plano de contratação (perfil, sourcing, entrevista, oferta)
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *contratar

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@chro
*contratar
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `função + requisitos + orçamento` | string | Yes | função + requisitos + orçamento |

## Output

- **plano de contratação (perfil, sourcing, entrevista, oferta)**: plano de contratação (perfil, sourcing, entrevista, oferta)

## Origin

Confidence: 87%
