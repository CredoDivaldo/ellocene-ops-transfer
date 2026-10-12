---
task: "Documentar Processo"
responsavel: "@processos"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - spec YAML + prosa (outbox ou já desenhado)
Saida: |
  - Ellocene/Document Tipo Runbook (Description = YAML + prosa); entidade Processo se a base existir
Checklist:
  - "[ ] Validar spec antes de gravar"
  - "[ ] create_entities Ellocene/Document: Tipo Runbook, Area Operacoes, Versao, Versao Principal"
  - "[ ] insert_document_blocks: bloco YAML process-spec + prosa canónica"
  - "[ ] Ligar EmpresaFilha; sem file:// em links"
  - "[ ] Se Ellocene/Processo não existir, declarar a limitação e usar o Document como índice"
  - "[ ] Handoff a docs só se o Credo pedir PDF e o estado for standard/activo"
---

# *documentar-processo

Materializa a fonte no Fibery. IMP-008. O PDF não é fonte.

## Usage

```
@processos
*documentar-processo {código ou spec}
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `código ou spec` | string | Yes | `PROC-…` já desenhado, ou spec colado |

## Output

URL Fibery do Document. Estado workflow: Rascunho. Campo `Ellocene/Codigo` = id do spec.

## Não feito se

Só `.md` local com MCP disponível; PDF como único artefacto; entidade vazia.
