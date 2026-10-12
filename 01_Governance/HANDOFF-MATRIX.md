# Matriz de Handoffs

| De | Para | Trigger | Payload |
|---|---|---|---|
| guardiao | especialista | pedido classificado | objectivo, contexto, definição de feito |
| actas | planos / registo | decisão ou tarefa confirmada | dono, prazo, fonte |
| planos | kpis | plano requer meta ou medição | métrica, cadência, dono |
| kpis | relatorios / guardiao | risco ou alteração material | valor, limiar, evidência |
| portfolio | legal / governanca | estrutura ou constituição | proposta, critérios, lacunas |
| legal | governanca / docs | minuta validável | base legal, revisão necessária |
| governanca | docs / guardiao | acto aprovado ou bloqueado | gate, evidência, próximo passo |
| relatorios | docs | relatório para público externo | conteúdo, público, identidade |
| processos | guardiao / docs | spec aprovado | trigger, owner, versão |
| ceo/cfo/cto/cmo/chro/cro | guardiao | recomendação accionável | opções, decisão, dono, prazo |

Para qualquer par não listado, usar `guardiao` como coordenador.
