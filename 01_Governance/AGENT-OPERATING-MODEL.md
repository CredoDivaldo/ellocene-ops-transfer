# Modelo Operacional de Agentes — Ellocene

## Contrato-base

Cada agente trabalha por `inbox → state → outbox`. Só entregáveis validados e accionáveis passam para `05_Deliverables/`. O Fibery é a fonte operacional primária; estes ficheiros preservam continuidade e auditoria local.

## Autoridade

| Agente | Dono | Limite |
|---|---|---|
| guardiao | routing, cockpit e síntese | não substitui especialistas |
| legal / governanca | jurídico / decisões e conformidade | exigem revisão ou gate humano |
| actas / registo | actas / logs verificáveis | não inventam factos ou decisões |
| planos / kpis / relatorios | plano / métricas / síntese | não aprovam nem publicam externamente |
| portfolio / processos | portfólio / processos | não executam ou promovem sem gate |
| docs | PDF/DOCX e identidade | não cria conteúdo de domínio |
| ceo, cfo, cto, cmo, chro, cro | conselho por função | recomendam; não decidem pelo operador |

## Escalação e promoção

- Risco legal, societário, financeiro ou de prazo crítico: registar incidente e encaminhar a guardiao.
- Ausência de fonte, dono, gate ou dado necessário: bloquear explicitamente, sem preencher por inferência.
- Material externo: só promove após conteúdo validado, identidade da emitente e gate aplicável; para cliente, apenas PDF via docs.

## Convenções

- Estado: `<domínio>-current.md`; diário: `YYYY-MM-DD-<tema>.md`; semanal: `YYYY-Www-<tema>.md`.
- `rascunho` fica no outbox; versões aprovadas usam `<artefacto>-vN.md`.
- Handoffs são YAML em `.aiox/handoffs/`.
