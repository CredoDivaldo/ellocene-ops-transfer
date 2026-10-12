---
task: "Listar Orfaos"
responsavel: "@governanca"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - âmbito (Fibery, Drive, ambos)
Saida: |
  - ficheiros/entidades sem dono ou referência
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *listar-orfaos

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@governanca
*listar-orfaos
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `âmbito (Fibery, Drive, ambos)` | string | Yes | âmbito (Fibery, Drive, ambos) |

## Output

- **ficheiros/entidades sem dono ou referência**: ficheiros/entidades sem dono ou referência

## Origin

Confidence: 90%
