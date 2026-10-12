---
task: "Registar Decisao"
responsavel: "@governanca"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - decisão + tipo (corrente/fundamental/existencial) + aprovadores
Saida: |
  - entidade Ellocene/Document (Tipo: Memo Decisao) + workflow conforme pacto (maioria/2-3/unanimidade)
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *registar-decisao

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@governanca
*registar-decisao
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `decisão + tipo (corrente/fundamental/existencial) + aprovadores` | string | Yes | decisão + tipo (corrente/fundamental/existencial) + aprovadores |

## Output

- **entidade Ellocene/Document (Tipo: Memo Decisao) + workflow conforme pacto (maioria/2-3/unanimidade)**: entidade Ellocene/Document (Tipo: Memo Decisao) + workflow conforme pacto (maioria/2-3/unanimidade)

## Origin

Confidence: 92%
