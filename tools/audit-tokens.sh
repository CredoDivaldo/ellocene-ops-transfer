#!/usr/bin/env bash
# audit-tokens.sh — gate de identidade visual do squad ellocene-ops
# ───────────────────────────────────────────────────────────────
# Uso:  tools/audit-tokens.sh <ficheiro.html> [mais ficheiros ...]
#
# Falha (exit 1) se algum var(--token) consumido não estiver declarado
# no mesmo ficheiro. Documentos que não usam paleta de marca (ex.:
# contratos formais da holding, enquanto os tokens da Holding não
# estiverem recolhidos) declaram os seus próprios tokens no :root.
#
# Este gate é obrigatório antes de qualquer PDF ir para cliente
# (config/governanca-documentos.md, regra 4 de identidades-empresas.yaml).
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "uso: $0 <ficheiro.html> [mais ficheiros ...]" >&2
  exit 2
fi

status=0
for f in "$@"; do
  if [[ ! -f "$f" ]]; then
    echo "✗ não existe: $f" >&2
    status=1
    continue
  fi

  defined="$(mktemp)"
  used="$(mktemp)"

  # tokens declarados (linhas `--nome:` dentro de qualquer bloco CSS)
  grep -oE "^[[:space:]]*--[a-zA-Z0-9-]+[[:space:]]*:" "$f" \
    | sed -E 's/^[[:space:]]*//; s/[[:space:]]*:$//' \
    | sort -u > "$defined" || true

  # tokens consumidos (var(--nome))
  grep -oE "var\(--[a-zA-Z0-9-]+" "$f" \
    | sed -E 's/^var\(//' \
    | sort -u > "$used" || true

  missing="$(comm -23 "$used" "$defined" || true)"

  if [[ -n "$missing" ]]; then
    echo "✗ $f: tokens consumidos mas não definidos:" >&2
    echo "$missing" | sed 's/^/    /' >&2
    echo "  Declara o token no :root deste ficheiro antes de gerar o PDF." >&2
    status=1
  else
    echo "✓ $f: $(wc -l < "$defined" | tr -d ' ') tokens declarados, $(wc -l < "$used" | tr -d ' ') consumidos"
  fi

  rm -f "$defined" "$used"
done

exit $status
