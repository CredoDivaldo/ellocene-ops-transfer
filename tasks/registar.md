---
task: "Registar"
responsavel: "@registo"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - input verbal do Credo
Saida: |
  - entrada Ellocene/Document (Tipo: Log) ligada a filha/projecto
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *registar

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@registo
*registar
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `input verbal do Credo` | string | Yes | input verbal do Credo |

## Output

- **entrada Ellocene/Document (Tipo: Log) ligada a filha/projecto**: entrada Ellocene/Document (Tipo: Log) ligada a filha/projecto

## Origin

Confidence: 95%
