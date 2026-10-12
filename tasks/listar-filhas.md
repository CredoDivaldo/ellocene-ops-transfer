---
task: "Listar Filhas"
responsavel: "@portfolio"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - filtros (estado, sector)
Saida: |
  - lista estruturada de EmpresaFilha
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *listar-filhas

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@portfolio
*listar-filhas
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `filtros (estado, sector)` | string | Yes | filtros (estado, sector) |

## Output

- **lista estruturada de EmpresaFilha**: lista estruturada de EmpresaFilha

## Origin

Confidence: 96%
