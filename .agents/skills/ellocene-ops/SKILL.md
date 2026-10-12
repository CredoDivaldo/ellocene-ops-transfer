---
name: ellocene-ops
description: Router da squad ellocene-ops — Cérebro operacional e de conselho da holding Ellocene (Guardião, Actas, Planos, Registo, Relatórios, Governança, KPIs, Portfolio, Docs, Processos, Legal + Conselho CEO/CFO/CTO/CMO/CHRO/CRO). Use sempre que o operador (Credo) activar um agente, pedir fluxo da holding OU mencionar conselho de administração, governança, contratos, KPIs, reuniões, actas, relatórios, processos, SOPs ou qualquer operação Ellocene/* no Fibery. Ponto de entrada único para a squad.
fonte_canonica: /Users/user/20_Areas/ELLOCENE/ellocene-ops
---

# ellocene-ops — Router (Aside / Claude)

Router da squad ellocene-ops. Encaminha para o agente adequado:

| Pedido sobre… | Encaminhar para |
|---|---|
| Status, cockpit, delegation, fluxos completos, handoffs | `guardiao` |
| Actas, reuniões, decisões, publicar acta | `actas` |
| Planos semanais, boot-dia, checkpoint, tarefas do dia | `planos` |
| Registo, log, sinalizar tarefa/desvio | `registo` |
| Relatórios holding/filha/investidor, state-of-the-union | `relatorios` |
| Decisões de governança, acta de sócios, auditoria Fibery, conformidade | `governanca` |
| KPIs: definir, medir, risco, importar metas | `kpis` |
| Nova filha, estado de portfólio, regra dos três | `portfolio` |
| PDF/DOCX, dossiê, proposta, SOP visual | `docs` |
| Detectar, desenhar, editar ou auditar processos e SOPs de conteúdo | `processos` |
| **Contratos, pacto social, SCP, deliberações, risco legal (lei angolana)** | `legal` |
| **Conselho estratégico / decisões do CEO** | `ceo` |
| **Conselho financeiro / unit economics / fiscal** | `cfo` |
| **Conselho técnico / arquitectura / roadmap / IA** | `cto` |
| **Conselho marketing / posicionamento / growth** | `cmo` |
| **Conselho pessoas / cultura / contratação** | `chro` |
| **Conselho comercial / receita / pricing** | `cro` |

## Regra inegociável — deliverables para cliente

Todo e qualquer documento destinado a ser enviado a um **CLIENTE** é entregue em **PDF** (via `docs`/WeasyPrint, identidade da filha emitente). `.md` é rascunho interno — nunca vai para a pasta do cliente nem é entregue ao cliente.

## Modo de uso

- `@guardiao *status` — visão geral de todos os processos.
- `@guardiao *delegar {pedido}` — delega para o agente certo.
- `@guardiao *cockpit` — visão 360 da holding.
- `@ceo *aconselhar {pergunta}` — conselho estratégico (com pesquisa).
- `@legal *redigir-contrato {tipo}` — minuta de contrato.
- `@processos *desenhar-processo {objectivo}` — criar um processo executável.

## Fonte canónica

O squad vive em `/Users/user/20_Areas/ELLOCENE/ellocene-ops`:

- `squad.yaml` — manifesto.
- `agents/*.md` — definições completas de cada agente.
- `tasks/*.md` — tasks por domínio.
- `data/` — biblioteca de conhecimento, identidades, nomenclatura.
- `config/` — tech-stack, coding-standards, source-tree.