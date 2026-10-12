# Matriz de I/O dos Agentes

| Agente | Entrada | Estado | Saída / promoção |
|---|---|---|---|
| guardiao | pedidos, sinais dos agentes | cockpit-current | routing, cockpit, plano de recuperação |
| legal | factos, pedido, fontes | legal-current | minuta ou parecer para revisão |
| governanca | proposta, provas, pacto | governanca-current | memo, acta, auditoria |
| actas | transcrição e contexto | actas-current | acta, decisões e tarefas |
| planos | prioridades e compromissos | planos-current | plano diário/semanal |
| registo | evento e fonte | registo-current | log e sinalização |
| portfolio | critérios e dados de filha | portfolio-current | avaliação e estado |
| kpis | definição, medição e fonte | kpis-current | KPI, medição, alerta |
| relatorios | dados datados e fontes | relatorios-current | relatório estruturado |
| docs | conteúdo validado e identidade | docs-current | PDF/DOCX aprovado |
| processos | processo, owner e trigger | processos-current | process spec e SOP validado |
| ceo | decisão estratégica | ceo-current | recomendação estratégica |
| cfo | dados financeiros | cfo-current | análise e cenários |
| cto | requisitos e restrições | cto-current | recomendação técnica |
| cmo | público, marca e dados | cmo-current | plano de marketing |
| chro | contexto de pessoas | chro-current | recomendação organizacional |
| cro | ICP, pipeline e dados | cro-current | plano comercial |

Toda saída que altere prioridade, dependa de outro agente ou fique bloqueada exige handoff.
