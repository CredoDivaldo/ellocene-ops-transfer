"""
generator.py — Motor determinístico de geração de documentos
Recebe: empresa + tipo de documento + variáveis
Devolve: caminhos de HTML e PDF gerados em segundos
"""

import os
import re
import sys
import time
import subprocess
from pathlib import Path
from typing import Dict, Any, Optional, Tuple

from registry import get_template_path, extract_placeholders, get_company_tokens_css
from validator import validate_variables, assert_no_leaked_placeholders, ValidationError

def inject_tokens_css(html_content: str, tokens_css: str) -> str:
    """
    Injecta o CSS de tokens no <head> do HTML.
    Se o HTML já tiver um :root {...} genérico, substitui-o pelo :root dos tokens da empresa.
    """
    if not tokens_css:
        return html_content

    # Se já tem :root no HTML, substitui o bloco :root
    pattern_root = re.compile(r':root\s*\{[^}]*\}', re.DOTALL)
    if pattern_root.search(html_content):
        # Extrai só o bloco :root dos tokens
        match = re.search(r':root\s*\{[^}]*\}', tokens_css, re.DOTALL)
        if match:
            new_root = match.group(0)
            return pattern_root.sub(new_root, html_content, count=1)

    # Se não tem ou não conseguiu substituir, injecta logo antes de </head>
    injection = f"\n<style>\n/* INJECTED DESIGN TOKENS */\n{tokens_css}\n</style>\n</head>"
    return html_content.replace("</head>", injection, 1)

def substitute_placeholders(content: str, variables: Dict[str, Any]) -> str:
    """Substitui [[KEY]] e {{KEY}} pelas variáveis fornecidas."""
    result = content
    for key, val in variables.items():
        val_str = str(val) if val is not None else ""
        # Formatos suportados: [[KEY]], {{KEY}}, e variantes com traço/underscore
        patterns = [
            f"[[{key}]]",
            f"[[{key.upper()}]]",
            f"[[{key.lower()}]]",
            f"{{{{{key}}}}}",
            f"{{{{{key.upper()}}}}}",
            f"{{{{{key.lower()}}}}}",
        ]
        for p in patterns:
            result = result.replace(p, val_str)
    return result

def generate_document(
    company: str,
    doc_type: str,
    variables: Dict[str, Any],
    output_dir: Optional[Path] = None,
    output_basename: Optional[str] = None,
    strict: bool = True,
) -> Dict[str, Any]:
    """
    Função principal de geração.
    Retorna dicionário com metadata, tempo de execução, e caminhos dos ficheiros.
    """
    start_time = time.time()

    # 1. Resolve template
    template_path = get_template_path(company, doc_type)
    if not template_path:
        raise FileNotFoundError(f"Template não encontrado para empresa='{company}', tipo='{doc_type}'")

    raw_template = template_path.read_text(encoding="utf-8")

    # 2. Extrai e valida placeholders
    placeholders = extract_placeholders(raw_template)
    if strict and placeholders:
        is_valid, missing = validate_variables(placeholders, variables)
        if not is_valid:
            raise ValidationError(missing)

    # 3. Injecta tokens CSS da empresa
    tokens_css = get_company_tokens_css(company)
    html_with_tokens = inject_tokens_css(raw_template, tokens_css) if tokens_css else raw_template

    # 4. Substitui variáveis
    rendered_html = substitute_placeholders(html_with_tokens, variables)

    # 5. Valida que nenhum placeholder sobreviveu
    leaked = assert_no_leaked_placeholders(rendered_html)
    if leaked:
        raise ValueError(f"Placeholders não substituídos no documento final: {leaked}")

    # 6. Determina directório e nomes de saída
    if not output_dir:
        output_dir = Path("/tmp/doc-engine-output")
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if not output_basename:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        output_basename = f"{company}-{doc_type}-{timestamp}"

    html_out_path = output_dir / f"{output_basename}.html"
    pdf_out_path = output_dir / f"{output_basename}.pdf"

    # 7. Grava HTML renderizado
    html_out_path.write_text(rendered_html, encoding="utf-8")

    # 8. Compila PDF via WeasyPrint
    weasy_cmd = ["weasyprint", str(html_out_path), str(pdf_out_path)]
    weasy_start = time.time()
    res = subprocess.run(weasy_cmd, capture_output=True, text=True)
    weasy_duration = time.time() - weasy_start

    if res.returncode != 0:
        raise RuntimeError(f"WeasyPrint falhou com código {res.returncode}:\n{res.stderr}")

    total_duration = time.time() - start_time

    return {
        "status": "success",
        "company": company,
        "document_type": doc_type,
        "template_source": str(template_path),
        "html_path": str(html_out_path),
        "pdf_path": str(pdf_out_path),
        "pdf_size_bytes": pdf_out_path.stat().st_size if pdf_out_path.exists() else 0,
        "weasyprint_duration_seconds": round(weasy_duration, 2),
        "total_duration_seconds": round(total_duration, 2),
    }
