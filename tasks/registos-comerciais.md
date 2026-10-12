---
task: "Registos Comerciais"
responsavel: "@legal"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - tipo de registo (constituição, alteração, NIF, sedes)
Saida: |
  - checklist + documentos necessários + sequência na Conservatória
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *registos-comerciais

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@legal
*registos-comerciais
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tipo de registo (constituição, alteração, NIF, sedes)` | string | Yes | tipo de registo (constituição, alteração, NIF, sedes) |

## Output

- **checklist + documentos necessários + sequência na Conservatória**: checklist + documentos necessários + sequência na Conservatória

## Origin

Confidence: 84%
