---
task: "Ver Registo Projecto"
responsavel: "@registo"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - projecto + período
Saida: |
  - histórico de registos do projecto
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *ver-registo-projecto

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@registo
*ver-registo-projecto
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `projecto + período` | string | Yes | projecto + período |

## Output

- **histórico de registos do projecto**: histórico de registos do projecto

## Origin

Confidence: 94%
