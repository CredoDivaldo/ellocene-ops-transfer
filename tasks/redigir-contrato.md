---
task: "Redigir Contrato"
responsavel: "@legal"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - tipo de contrato + partes + termos principais
Saida: |
  - minuta de contrato (pt-AO) sólida, com cláusulas standard + específicas, pronta para revisão de advogado
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *redigir-contrato

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@legal
*redigir-contrato
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tipo de contrato + partes + termos principais` | string | Yes | tipo de contrato + partes + termos principais |

## Output

- **minuta de contrato (pt-AO) sólida, com cláusulas standard + específicas, pronta para revisão de advogado**: minuta de contrato (pt-AO) sólida, com cláusulas standard + específicas, pronta para revisão de advogado

## Origin

Confidence: 88%
