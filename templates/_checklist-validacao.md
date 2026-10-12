# Checklist de Validação de Novo Template
# Padrão binário pass/fail (qualquer FAIL bloqueia activação do template)

## 1. Identidade e Design System
- [ ] Empresa existe em `data/design-systems/` com `tokens.json` e CSS gerado
- [ ] Cores NÃO estão hardcoded no template — são consumidas via `var(--...)`
- [ ] Script `audit-tokens.sh` executado sobre o template com resultado `✓ exit 0`
- [ ] Tipografia respeita a marca (ex: Michroma/Raleway p/ Tivra; Geist p/ Blimari; Sans fina p/ Altars)
- [ ] Regras de proibições da marca respeitadas (ex: Altars proíbe fundos escuros e branco puro)

## 2. Conteúdo e Estrutura
- [ ] Inventário de placeholders `[[NOME]]` está fechado e documentado no `.yaml` correspondente
- [ ] Nenhuma menção a equipa interna da holding ou decisões privadas em documentos de cliente
- [ ] Se o documento tiver valor contratual/jurídico: revisto pelo `@legal` antes da aprovação
- [ ] Formatação compatível com WeasyPrint (A4, paginação `@bottom-right`, sem overflow de margens)

## 3. Registos e Governança (IMP-008 / IMP-009)
- [ ] Template registado no Fibery (`Ellocene/Document`) com `Tipo de Documento = Template`
- [ ] Estado inicial no Fibery: `Rascunho` ou `Aguardando Aprovacao`
- [ ] Campo `Aprovado por` e `Data de Aprovacao` preenchidos pelo Credo antes de passar a `Activo`
- [ ] Links no Fibery são estritamente URLs Web/Drive (zero `file:///` ou paths locais)
