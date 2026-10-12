---
task: "Preparar Pitch"
responsavel: "@ceo"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - tipo (investidor, cliente enterprise, banco) + alvo
Saida: |
  - estrutura de pitch + mensagens-chave + objecções
Checklist:
  - "[ ] Validate input parameters"
  - "[ ] Execute main logic"
  - "[ ] Format output"
  - "[ ] Return result"
---

# *preparar-pitch

Task generated from squad design blueprint for ellocene-ops.

## Usage

```
@ceo
*preparar-pitch
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tipo (investidor, cliente enterprise, banco) + alvo` | string | Yes | tipo (investidor, cliente enterprise, banco) + alvo |

## Output

- **estrutura de pitch + mensagens-chave + objecções**: estrutura de pitch + mensagens-chave + objecções

## Origin

Confidence: 89%
