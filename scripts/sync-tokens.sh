#!/usr/bin/env bash
#
# sync-tokens.sh — Sincroniza design tokens vendored para dentro do ellocene-ops
# ─────────────────────────────────────────────────────────────────────────────
# Copia os tokens CSS e SVGs de cada empresa do repo Altars-Group/design-systems
# para data/design-systems/, gerando um MANIFEST.md com os hashes md5.
#
# Uso:
#   scripts/sync-tokens.sh [caminho-local-do-repo]
#   scripts/sync-tokens.sh                  # default: ~/10_Projects/design-systems
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SQUAD_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SOURCE="${1:-$HOME/10_Projects/design-systems}"
DEST="$SQUAD_DIR/data/design-systems"

if [ ! -d "$SOURCE" ]; then
  echo "✗ Erro: directório fonte não encontrado em $SOURCE" >&2
  exit 1
fi

echo "Sincronizando design systems de: $SOURCE"
echo "Destino: $DEST"

mkdir -p "$DEST"

# Empresas
COMPANIES=("holding" "blimari" "altars" "tivra" "piramyd" "aicos")

MANIFEST="$DEST/MANIFEST.md"
cat << 'EOF' > "$MANIFEST"
# Design Systems — Manifest Vendored

> Cópia sincronizada de `Altars-Group/design-systems`.
> Fonte única de verdade: https://github.com/Altars-Group/design-systems
> Não editar estes ficheiros directamente. Edite no repo fonte e corra `scripts/sync-tokens.sh`.

EOF

echo "Sincronizado em: $(date -u +"%Y-%m-%dT%H:%M:%SZ")" >> "$MANIFEST"
echo "" >> "$MANIFEST"
echo "| Empresa | Ficheiro | MD5 |" >> "$MANIFEST"
echo "|---|---|---|" >> "$MANIFEST"

COUNT=0

for c in "${COMPANIES[@]}"; do
  SRC_C="$SOURCE/$c"
  [ -d "$SRC_C" ] || continue

  DEST_C="$DEST/$c"
  mkdir -p "$DEST_C"

  # Copia .css, .print.css, .tokens.json, .svg (suporta espaços em nomes)
  while IFS= read -r -d '' f; do
    REL="${f#$SRC_C/}"
    TARGET_FILE="$DEST_C/$REL"
    mkdir -p "$(dirname "$TARGET_FILE")"
    cp "$f" "$TARGET_FILE"

    # Regista hash
    HASH=$(md5 -q "$TARGET_FILE" 2>/dev/null || md5sum "$TARGET_FILE" | cut -d' ' -f1)
    echo "| $c | $REL | \`$HASH\` |" >> "$MANIFEST"
    COUNT=$((COUNT + 1))
  done < <(find "$SRC_C" -type f \( -name "*.css" -o -name "*.json" -o -name "*.svg" \) -print0 2>/dev/null)

  echo "  ✓ $c sincronizado"
done

echo "" >> "$MANIFEST"
echo "Total de ficheiros sincronizados: $COUNT" >> "$MANIFEST"

echo ""
echo "✓ Sync concluído: $COUNT ficheiros em $DEST"
echo "✓ Manifesto gerado em: $MANIFEST"
