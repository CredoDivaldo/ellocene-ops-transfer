---
task: "Ver Registo Dia"
responsavel: "@registo"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - data (default: hoje)
Saida: |
  - registos do dia agrupados por filha/projecto
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *ver-registo-dia

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@registo
*ver-registo-dia
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `data (default: hoje)` | string | Yes | data (default: hoje) |

## Output

- **registos do dia agrupados por filha/projecto**: registos do dia agrupados por filha/projecto

## Origin

Confidence: 96%
