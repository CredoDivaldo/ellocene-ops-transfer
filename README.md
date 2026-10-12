# ellocene-ops — Squad de Gestão 360 da Holding Ellocene

Squad (AIOX) que automatiza e padroniza a operação da holding Ellocene sobre o Fibery (`Ellocene/*`): governança, reuniões, decisões, planeamento, logging, relatórios, portfólio de EmpresaFilhas, KPIs, documentação — **mais** um **Conselho de Administração** (CEO/CFO/CTO/CMO/CHRO/CRO) que dá conselho de leverage com conhecimento pesquisado dinamicamente (livros, legislação, mercados), e um **Conselheiro Jurídico Angolano** (@legal).

## Camadas

| Camada | Agentes | Propósito |
|--------|---------|-----------|
| **Orquestração** | @guardiao | Entrada única, cockpit 360, routing, fluxos ponta-a-ponta |
| **Operacional** | @actas @planos @registo @relatorios @docs @processos @governanca @portfolio @kpis | Automatizar processos diários sobre o Fibery |
| **Jurídico** | @legal | Contratos, pactos, SCP, deliberações, registos — lei angolana |
| **Conselho** | @ceo @cfo @cto @cmo @chro @cro | Conselho estratégico estilo YC/SV, pesquisa dinâmica de conhecimento |

## Quick Start

```
@guardiao *status                      # Estado de todos os processos
@guardiao *cockpit                     # Visão 360 da holding
@guardiao *delegar {pedido}            # Delegar para o agente correcto
@actas *gerar-acta {transcricao}       # Gerar acta de reunião
@ceo *aconselhar {pergunta}            # Conselho estratégico
@legal *redigir-contrato {tipo}        # Minuta de contrato
@guardiao *fluxo-conselho-decisao      # Fluxo completo conselho → decisão → documento
@planos *boot-dia                      # Cockpit diário
@processos *detectar-processos         # Inventário de processos
@processos *desenhar-processo {x}      # Criar Process Spec executável
```

## Fluxos Completos

Ver `01_Governance/WORKFLOW-ORCHESTRATION.md` — F1 a F6 (conselho→decisão, contrato, nova filha, reporting sócios, planeamento, investidor).

## Operador

**Credo** (CEO) — operador exclusivo.

## Integrações

- **Fibery** (MCP) — memória executiva: EmpresaFilha, Client, Project, Task, Meeting, Document, Financeiro, KPI, MarketingEditorial, Socio
- **Google Drive** (`/Users/user/Library/CloudStorage/GoogleDrive-blimariapp@gmail.com/My Drive/ELLOCENE`) — repositório documental (dados da holding e empresas-filhas)
- **WeasyPrint / Pandoc / python-docx** — PDF e DOCX com identidade por empresa
- **Biblioteca de Conhecimento** — livros + legislação angolana + web (pesquisa dinâmica)

## Princípios

1. TUDO é auditável — cada acção gera registo verificável
2. TUDO deixa rasto — logs, timestamps, ficheiros versionados
3. TUDO é padronizado — templates fixos, nomenclatura consistente
4. Separação de responsabilidades — cada agente dono do seu domínio
5. @docs é o único produtor de PDF/DOCX final, com **identidade por empresa**
6. @legal valida tudo com efeito jurídico; advogado revê antes de assinar
7. Conselheiros **pesquisam** (não inventam) e citam fontes
8. Governança da holding (maiorias/unanimidade) respeitada
9. Gates de aprovação humana nos pontos críticos

## Fontes de verdade

- Manifest: `squad.yaml`
- Governança: `01_Governance/`
- Estado operacional: `02_Control/<agente>/state/`
- Handoffs: `.aiox/handoffs/`
- Blueprint de design: `squads/.designs/ellocene-ops-squad-design.yaml`