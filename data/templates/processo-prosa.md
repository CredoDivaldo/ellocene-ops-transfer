# PROC-{DOMINIO}-{slug} — {Título no infinitivo: verbo + objecto}

| Campo | Valor |
|---|---|
| ID | PROC-{DOMINIO}-{slug} |
| Estado | rascunho \| em_revisao \| aprovado \| activo \| arquivado |
| Versão | {semver} |
| Dono (A) | {H:Nome} |
| EmpresaFilha / Holding | {Ellocene \| Altars \| Blimari \| Piramyd \| Tivra} |
| Trigger | {evento / limiar / calendário — frase testável} |
| Pause point | {quando abrir este documento} |
| Tipo de checklist | READ-DO \| DO-CONFIRM |
| Fibery | {URL Document — nunca file://} |
| Próxima revisão | {YYYY-MM-DD} |
| Golden run | {ligação à última execução correcta} |

## 1. Propósito
{Uma frase: resultado de negócio + porquê.}

## 2. Âmbito
- Cobre: {lista}
- Não cobre: {lista + ID do processo correcto}

## 3. Entradas
| Campo | Obrigatório | Origem | Se em falta |
|---|---|---|---|
| {campo} | sim/não | {ferramenta} | {default seguro OU parar + escalar} |

## 4. Papéis (RACI-A)
| Papel | Quem | Tipo H/A/S | R | A | C | I |
|---|---|---|---|---|---|---|
| {papel} | {nome} | {H\|A\|S} | | | | |

Regras: exactamente um A no processo. Agente MUST NOT ser A de gate jurídico/societário.

## 5. Passos
| # | Actor | Verbo + objecto | Ferramenta | Critério de feito | Ponto-chave | Razão |
|---|---|---|---|---|---|---|
| P1 | {H:… / A:@… / S:…} | {infinitivo + objecto} | {produto + ecrã/comando} | {binário, observável} | {faz/desfaz, gate, ou jeito} | {porque} |

RFC 2119:
- O executor MUST completar P-n na ordem, salvo ramo da secção 6.
- O executor MUST NOT {acção perigosa}.
- O executor SHOULD {padrão}.
- O executor MAY {juízo — só H, ou A com critério}.

## 6. Ramos
IF {condição objectiva} THEN {acção + processo ligado}
ELSE {default seguro} AND notificar {quem} via {canal}

## 7. Falha e rollback
| Falha | Como detectar | O que fazer | MUST NOT |
|---|---|---|---|
| {falha} | {sinal} | {runbook / passo} | {ex.: apagar linhas à mão} |

## 8. Critério de feito do processo
- Artefacto: {o quê, onde}
- Estado no sistema: {campo = valor}
- Evidência: {log / ID / URL}

## 9. Métrica
| Indicador | Fórmula | Limiar | Onde se lê |
|---|---|---|---|
| {nome} | {fórmula} | {verde/amarelo/vermelho} | {Fibery/KPI} |

## 10. Formação (TWI)
- Instrutor: {quem já executou 3x}
- Folha: a tabela da secção 5 = Job Breakdown
- Critério "sabe": o executor explica passo + ponto-chave + razão **enquanto faz**

## 11. Job aid (5–9 killer items)
- [ ] {item extraído dos passos, não inventado}

## 12. Changelog
| Versão | Data | O que mudou | Porquê |
|---|---|---|---|
| {n} | {data} | {diff} | {motivo de negócio} |
