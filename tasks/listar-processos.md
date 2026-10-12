---
task: "Listar Processos"
responsavel: "@processos"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - filtros opcionais (estado, filha, dono)
Saida: |
  - catálogo; declara se Ellocene/Processo ainda não existe
Checklist:
  - "[ ] Query Fibery Document Tipo Runbook com Codigo PROC-*"
  - "[ ] Se a base Ellocene/Processo existir, usá-la como índice"
  - "[ ] Incluir rascunhos no outbox local se MCP falhar"
  - "[ ] Declarar limitação de schema se a base não existir"
---

# *listar-processos

Catálogo filtrável. Não detecta (isso é `*detectar-processos`).

## Usage

```
@processos
*listar-processos {filtros}
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `filtros` | string | No | `estado:activo`, `filha:BLI`, `dono:credo` |

## Output

Tabela: id, título, estado, versão, dono, URL Fibery, próxima revisão.
