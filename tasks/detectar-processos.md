---
task: "Detectar Processos"
responsavel: "@processos"
responsavel_type: agent
atomic_layer: task
Entrada: |
  - âmbito opcional (squad | filha | hábitos | all)
Saida: |
  - inventário classificado (explícito / implícito / filha / hábito) sem marcar activo
Checklist:
  - "[ ] Varrer ellocene-ops/tasks/fluxo-*.md e HANDOFF-MATRIX"
  - "[ ] Varrer Fibery Document Tipo Runbook/Checklist/Norma"
  - "[ ] Varrer .aiox/handoffs como log pobre (from/to/command)"
  - "[ ] Varrer manuais de filha e registo/WhatsApp se o âmbito incluir hábitos"
  - "[ ] Classificar cada candidato; nunca estado activo"
  - "[ ] Publicar Nota/tabela no Fibery (fallback: 02_Control/17_Processos/outbox)"
---

# *detectar-processos

Inventário de processos de jure vs de facto. Sem Celonis. Sem promover.

## Usage

```
@processos
*detectar-processos {âmbito}
```

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `âmbito` | string | No | `squad` (omissão), `filha:<código>`, `habitos`, `all` |

## Output

Tabela: código provisório, evidência, classificação, dono aparente, próxima acção (`desenhar` / `ignorar` / `já documentado`). Document Fibery Tipo Nota, estado Rascunho.

## Não feito se

Marcar `activo`; inventar BPMN; fingir process mining enterprise.
