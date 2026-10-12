---
task: "Fluxo Contrato"
responsavel: "@guardiao"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - necessidade de contrato (cliente, sócio, fornecedor, parceria)
Saida: |
  - cadeia: @legal (redigir-contrato) → @cro/@ceo (termos comerciais) → @legal (review) → gate Credo → @docs (DOCX identidade) → Governança
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *fluxo-contrato

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@guardiao
*fluxo-contrato
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `necessidade de contrato (cliente, sócio, fornecedor, parceria)` | string | Yes | necessidade de contrato (cliente, sócio, fornecedor, parceria) |

## Output

- **cadeia: @legal (redigir-contrato) → @cro/@ceo (termos comerciais) → @legal (review) → gate Credo → @docs (DOCX identidade) → Governança**: cadeia: @legal (redigir-contrato) → @cro/@ceo (termos comerciais) → @legal (review) → gate Credo → @docs (DOCX identidade) → Governança

## Origin

Confidence: 87%
