# PROC-HOL-registo-financeiro — 1 página

**Objectivo:** Nenhum dinheiro da empresa entra ou sai sem registo no Fibery no mesmo dia.

## Quem faz o quê
| Papel | Pessoa | Faz |
|-------|--------|-----|
| Accountable | **Credo** | Aprova saídas; fecha o dia; gate final |
| Executa pagamento | Credo (até haver conta BAI) | Transfere / paga |
| Comercial / pedido | Celson | Avisa receita de cliente; pede pagamento de ferramentas de marketing |
| Registo | Quem mexeu no dinheiro | Cria entidade Fibery + põe comprovativo no Drive |

## Os 5 casos (escolhe um)

### 1. Cliente vai pagar / pagou
1. Celson ou Credo cria `Ellocene/Financeiro` Tipo=Receita, Estado=Pendente, Valor, Cliente, Referência=nº factura.
2. Quando o dinheiro entra → screenshot/extracto → Drive `02-Financeiro/Comprovativos/YYYY-MM/`.
3. Estado → Confirmado. Referência actualizada.

### 2. Preciso pagar ferramenta / custo (requisição)
1. Quem precisa: mensagem curta a Credo (valor + motivo + link).
2. Credo aprova (ou paga ele próprio).
3. **Antes ou no acto do pagamento:** criar Financeiro Tipo=Custo Operacional (ou Custo Pessoal), Estado=Pendente.
4. Pagar → guardar comprovativo no Drive → Estado=Confirmado.

### 3. Custo equipa / almoço / operacional
Igual ao 2. Nome claro no Fibery (ex: "Almoço equipa 08-10").

### 4. Transferência inter-filha
Tipo=Transferencia Inter-Filha. Origem + Destino preenchidos. Comprovativo obrigatório.

### 5. Ajuste / saldo inicial / outro
Tipo=Outro. Referência explica o porquê (como o ponto zero de 80.000 AKZ).

## Onde guardar comprovativos
```
Drive/ELLOCENE/02-Financeiro/Comprovativos/YYYY-MM/
  2026-10-08-receita-cliente-X.png
  2026-10-08-custo-apify.pdf
```
Ou na pasta da filha: `06-Empresas-Filhas/<Nome>/02-Financeiro/...`

No Fibery campo **Referência**: nome do ficheiro ou URL Drive.

## Rotina diária (5 minutos — qualquer agente / ChatGPT / Claude / Grok)
Pergunta-chave para colar em qualquer AI:
> "Consulta Fibery Ellocene/Financeiro: pendentes >48h? Movimentos de hoje? Saldo mental (80k inicial ± movimentos Confirmados) vs realidade. Lista o que falta."

Se houver pendente >48h → resolver hoje.
Se movimento feito sem registo → criar retroactivo com nota "registo tardio".

## Regras de ouro (job-aid)
1. Fibery no mesmo dia do dinheiro.
2. Saída sem comprovativo = Pendente, não Confirmado.
3. Só Credo aprova saídas relevantes.
4. Até conta BAI: tudo ainda pode estar em conta pessoal — a Referência deve dizê-lo.
5. Segunda-feira: abrir BAI e transferir os 80k para a conta empresa.
