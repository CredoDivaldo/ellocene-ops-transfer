#!/usr/bin/env python3
"""
cli.py — Interface CLI do doc-engine
Permite gerar documentos a partir de JSON ou argumentos de linha de comandos.

Uso:
  python3 cli.py --company altars --type proposal --vars '{"CLIENTE-NAME": "Acme", ...}'
  python3 cli.py --company holding --type scp --vars-file dados.json --out-dir /path/to/folder
"""

import argparse
import json
import sys
from pathlib import Path

# Adiciona src ao path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from generator import generate_document
from registry import get_template_path, extract_placeholders

def main():
    parser = argparse.ArgumentParser(description="Motor determinístico de geração de documentos Ellocene")
    parser.add_argument("--company", required=True, help="Empresa (altars, blimari, tivra, holding, etc.)")
    parser.add_argument("--type", required=True, help="Tipo de documento (proposal, scp, contract, report, etc.)")
    parser.add_argument("--vars", help="JSON string com as variáveis")
    parser.add_argument("--vars-file", help="Caminho para ficheiro JSON com as variáveis")
    parser.add_argument("--out-dir", help="Directório de saída para os ficheiros HTML e PDF")
    parser.add_argument("--out-name", help="Nome base para os ficheiros (sem extensão)")
    parser.add_argument("--list-placeholders", action="store_true", help="Lista apenas os placeholders que o template exige")

    args = parser.parse_args()

    # Modo: listar placeholders
    if args.list_placeholders:
        tpl_path = get_template_path(args.company, args.type)
        if not tpl_path:
            print(f"Erro: template não encontrado para empresa='{args.company}', tipo='{args.type}'", file=sys.stderr)
            sys.exit(1)
        phs = extract_placeholders(tpl_path.read_text(encoding="utf-8"))
        print(f"Template: {tpl_path}")
        print(f"Placeholders necessários ({len(phs)}):")
        for p in phs:
            print(f"  - {p}")
        sys.exit(0)

    # Carrega variáveis
    variables = {}
    if args.vars:
        try:
            variables = json.loads(args.vars)
        except json.JSONDecodeError as e:
            print(f"Erro ao interpretar JSON de --vars: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.vars_file:
        vars_path = Path(args.vars_file)
        if not vars_path.exists():
            print(f"Ficheiro de variáveis não encontrado: {vars_path}", file=sys.stderr)
            sys.exit(1)
        variables = json.loads(vars_path.read_text(encoding="utf-8"))
    else:
        print("Erro: forneça --vars ou --vars-file (ou use --list-placeholders para ver o que falta)", file=sys.stderr)
        sys.exit(1)

    try:
        out_dir = Path(args.out_dir) if args.out_dir else None
        result = generate_document(
            company=args.company,
            doc_type=args.type,
            variables=variables,
            output_dir=out_dir,
            output_basename=args.out_name,
        )
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Erro: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
