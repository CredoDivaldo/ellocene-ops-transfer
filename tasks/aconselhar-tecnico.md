---
task: "Aconselhar Tecnico"
responsavel: "@cto"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - pergunta técnica/arquitectura do Credo
Saida: |
  - recomendação técnica + prós/contras + fontes
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *aconselhar-tecnico

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@cto
*aconselhar-tecnico
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pergunta técnica/arquitectura do Credo` | string | Yes | pergunta técnica/arquitectura do Credo |

## Output

- **recomendação técnica + prós/contras + fontes**: recomendação técnica + prós/contras + fontes

## Origin

Confidence: 90%
