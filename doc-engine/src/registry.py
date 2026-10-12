"""
registry.py — Catálogo de templates do doc-engine
Descobre templates HTML em ellocene-ops/templates/ e mapeia por empresa e tipo.
"""

from pathlib import Path
from typing import Dict, List, Optional
import re

SQUAD_DIR = Path(__file__).resolve().parent.parent.parent
TEMPLATES_DIR = SQUAD_DIR / "templates"
DESIGN_SYSTEMS_DIR = SQUAD_DIR / "data" / "design-systems"

# Mapeamento canónico de tipos de documento para ficheiros de template
TEMPLATE_MAP = {
    ("altars", "proposal"): "proposta-comercial-template.html",
    ("altars", "scp"): "contrato-scp-template.html",
    ("altars", "contract"): "contrato-scp-template.html",
    ("holding", "scp"): "contrato-scp-template.html",
    ("holding", "contract"): "contrato-scp-template.html",
    ("blimari", "proposal"): "proposta-comercial-template.html",
    ("tivra", "proposal"): "proposta-comercial-template.html",
}

def get_template_path(company: str, doc_type: str) -> Optional[Path]:
    """Retorna o caminho do ficheiro de template para a empresa e tipo."""
    company = company.lower()
    doc_type = doc_type.lower()

    # 1. Procura no mapa canónico
    filename = TEMPLATE_MAP.get((company, doc_type))
    if filename and (TEMPLATES_DIR / filename).exists():
        return TEMPLATES_DIR / filename

    # 2. Procura em subpasta da empresa (templates/{company}/{type}.html)
    company_subdir = TEMPLATES_DIR / company
    if company_subdir.exists():
        for ext in [".html", ".md"]:
            candidate = company_subdir / f"{doc_type}{ext}"
            if candidate.exists():
                return candidate

    # 3. Fallback: holding
    filename = TEMPLATE_MAP.get(("holding", doc_type))
    if filename and (TEMPLATES_DIR / filename).exists():
        return TEMPLATES_DIR / filename

    return None

def extract_placeholders(template_content: str) -> List[str]:
    """Extrai todos os placeholders no formato [[NOME]] ou {{NOME}} do template."""
    pattern_bracket = re.compile(r'\[\[([A-Z0-9_-]+)\]\]')
    pattern_mustache = re.compile(r'\{\{([A-Z0-9_-]+)\}\}')

    found = set(pattern_bracket.findall(template_content))
    found.update(pattern_mustache.findall(template_content))
    return sorted(list(found))

def get_company_tokens_css(company: str) -> Optional[str]:
    """Retorna o conteúdo do tokens.print.css da empresa a partir do vendored."""
    company = company.lower()
    company_dir = DESIGN_SYSTEMS_DIR / company

    if not company_dir.exists():
        # Fallback para holding
        company_dir = DESIGN_SYSTEMS_DIR / "holding"
        if not company_dir.exists():
            return None

    # Procura .print.css
    for candidate in [
        company_dir / f"{company}.print.css",
        company_dir / "tokens" / f"{company}.print.css",
        company_dir / f"{company}.css",
        company_dir / "tokens" / f"{company}.css",
    ]:
        if candidate.exists():
            return candidate.read_text(encoding="utf-8")

    return None
