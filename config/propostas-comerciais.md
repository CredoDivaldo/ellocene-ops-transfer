---
name: propostas-comerciais
description: "Padrão obrigatório de propostas comerciais do squad ellocene-ops (template, identidade, secções, modalidades de preço, gates e registo no Fibery)."
verificado_em: "2026-10-09"
fonte_produto: "Fibery Documento 102 (Parceria de Crescimento), Documento 22 (Método Aurora)"
---

# Propostas Comerciais — Padrão Obrigatório

Fonte canónica para TODA a proposta comercial enviada a cliente. Vale para o @cro, para o @docs e para qualquer agente ou pessoa que produza uma proposta. Não existem propostas fora deste padrão.

## 1. Regras obrigatórias

1. Toda a proposta usa o **template oficial da empresa emitente**. Para a Altars: `06-Empresas-Filhas/Altars/05-Marketing/Brand-Book/Proposta-TEMPLATE.html` (Google Drive, pasta ELLOCENE). Não se criam layouts novos.
2. A identidade visual vem do design system da emitente (`data/design-systems/`). Nenhum token é inventado.
3. O PDF é gerado pelo @docs (WeasyPrint, A4, fundo uniforme), **somente depois** de `tools/audit-tokens.sh <ficheiro.html>` terminar com exit 0.
4. A proposta é guardada na pasta do cliente no Google Drive (`04-Clientes/<Cliente>/04-Entregaveis/`). Nunca fica no Mac.
5. Registo obrigatório no Fibery (`Ellocene/Document`): Tipo de Documento "Proposta Comercial", ligado ao Projecto, à EmpresaFilha e ao Cliente. `Link Principal` = URL do PDF no Drive; `Pasta Drive` = URL da pasta do cliente; a `Description` tem o mesmo texto do PDF (versão homóloga).
6. O documento para cliente não contém notas internas, margens, custos internos, estratégia comercial nem comentários de revisão.
7. Validade padrão: **15 dias úteis** a partir da data de emissão.

## 2. Ordem fixa das secções

Capa · 01 Sumário Executivo · [opcional] 02 Contexto · O Problema · A Causa Raiz · A Nossa Promessa · O Método Aurora · [opcional] O que muda no dia-a-dia · [opcional] Plano e Cronograma · [opcional] Critérios de Sucesso · Investimento · O que está incluído e o que não está · Próximos Passos.

As secções opcionais removem-se quando não se aplicam. A numeração mantém-se sequencial.

## 3. Modalidades de preço

- **Subscrição mensal (padrão Altars, Parceria de Crescimento).** Taxa de entrada 0 Kz; facturação no início de cada período de 30 dias; sem fidelização forçada; o primeiro mês cobre construção e implementação. Fonte: Fibery Documento 102.
- **Projecto (entrega única com pagamento em prestações).** Não estava previsto nesta fonte. Fica registado como excepção provisória, aprovada pelo Credo a 2026-10-09 no caso Okanda Pay: 50% na assinatura do Anexo A e 50% após a entrada em operação, com suporte incluído no preço. A proposta de projecto remete sempre para o contrato de prestação de serviços e para o Anexo A, e nunca dispensa esse contrato.

## 4. Linguagem

- Português de Angola. Kwanzas (Kz) com espaço como separador de milhar (`Kz 350 000`).
- Sem anglicismos: go-live → entrada em operação; dashboard → painel; workshop → sessão de trabalho; pipeline → carteira.
- Sem jargão de consultoria. Tom humano e directo.

## 5. Garantias

A garantia de resultados (mês gratuito, quando não há nenhum resultado por causa da Altars) é exclusiva da Parceria de Crescimento (Fibery Documento 102). Não se transpõe para projectos sem decisão escrita do Credo.

## 6. Processo de produção (ordem obrigatória)

1. @cro prepara o conteúdo e a modalidade de preço. O Credo aprova os valores.
2. Copiar o template para `04-Clientes/<Cliente>/04-Entregaveis/Proposta-<Emitente>-<Cliente>.html`. Substituir os marcadores, renumerar as secções, remover as opcionais.
3. `tools/audit-tokens.sh <ficheiro.html>`: exit 0 é obrigatório.
4. @docs gera o PDF com WeasyPrint directamente no Drive. Enquanto não estiver aprovada, o nome tem o sufixo `-RASCUNHO`.
5. Registo no Fibery, conforme a regra 5.
6. Envio ao cliente só depois do gate do Credo.

## 7. Histórico

- 2026-09-25: Parceria de Crescimento (Documento 102) aprovada como fonte do produto.
- 2026-10-09: padrão de propostas tornado obrigatório. Gate de auditoria restaurado em `tools/audit-tokens.sh`. Modalidade de projecto registada como excepção provisória.
