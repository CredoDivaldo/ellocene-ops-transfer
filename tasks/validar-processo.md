---
task: "Validar Processo"
responsavel: "@processos"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - código PROC-… ou spec
Saida: |
  - checklist pass/fail binário por item
Checklist:
  - "[ ] Correr ellocene-ops/data/templates/checklist-validacao.md mecanicamente"
  - "[ ] Confirmar comandos contra ellocene-ops/agents/*.md"
  - "[ ] Confirmar alinhamento YAML ↔ prosa"
  - "[ ] Confirmar que rascunho não está a ser usado como activo"
  - "[ ] Devolver FAIL com a lista exacta; não 'quase passa'"
---

# *validar-processo

Evaluator-optimizer do spec. Binário.

## Usage

```
@processos
*validar-processo {PROC-…}
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `código ou spec` | string | Yes | Processo a validar |

## Output

PASS ou FAIL + itens. FAIL bloqueia `*promover-processo`.
