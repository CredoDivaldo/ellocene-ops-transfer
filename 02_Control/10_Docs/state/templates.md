# Estado dos Templates de Documentos — Control State

> Mantido pelo `@docs`. Actualizado em: 2026-09-25.
> Fonte de design tokens: `Altars-Group/design-systems` (vendored em `data/design-systems/`).

## Catálogo de Templates

| ID | Empresa | Tipo Documento | Ficheiro HTML | Audit Tokens | Estado |
|---|---|---|---|---|---|
| `TPL-ALT-proposta-comercial` | Altars | `proposal` | `proposta-comercial-template.html` | ✓ PASS | 🟢 Activo |
| `TPL-ALT-contrato-scp` | Altars | `scp` / `contract` | `contrato-scp-template.html` | ✓ PASS | 🟢 Activo |
| `TPL-HOL-contrato-scp` | Holding | `scp` / `contract` | `contrato-scp-template.html` | ✓ PASS | 🟢 Activo |
| `TPL-BLI-proposta-comercial` | Blimari | `proposal` | `proposta-comercial-template.html` | ✓ PASS | 🟡 Em testes |
| `TPL-TIV-proposta-comercial` | Tivra | `proposal` | `proposta-comercial-template.html` | ✓ PASS | 🟡 Em testes |

## Histórico de Auditoria
- **2026-09-25:** Correcção do bug crítico de `--gold-deep` e `--panel` no template de proposta. Audit automático passou a 100% de sucesso.
- **2026-09-25:** Integração com motor determinístico `doc-engine/` (geração de PDF em 2.8 segundos).
