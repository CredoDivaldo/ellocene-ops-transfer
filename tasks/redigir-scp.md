---
task: "Redigir Scp"
responsavel: "@legal"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - participante + % + activos + termos
Saida: |
  - minuta de Sociedade em Conta de Participação (SCP) + risco fiscal
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *redigir-scp

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@legal
*redigir-scp
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `participante + % + activos + termos` | string | Yes | participante + % + activos + termos |

## Output

- **minuta de Sociedade em Conta de Participação (SCP) + risco fiscal**: minuta de Sociedade em Conta de Participação (SCP) + risco fiscal

## Origin

Confidence: 85%
