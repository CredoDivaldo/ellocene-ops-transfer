"""
validator.py — Validação rigorosa de input e output no doc-engine
Princípio: se faltar um dado obrigatório, RECUSA com lista de falhas.
Nunca gera um documento incompleto ou com [[PLACEHOLDER]] visível.
"""

from typing import Dict, List, Tuple
import re

class ValidationError(Exception):
    def __init__(self, missing_fields: List[str]):
        self.missing_fields = missing_fields
        msg = f"Validação falhou. Faltam os seguintes campos obrigatórios:\n" + "\n".join(f"  - {f}" for f in missing_fields)
        super().__init__(msg)

def validate_variables(required_placeholders: List[str], provided_vars: Dict[str, str]) -> Tuple[bool, List[str]]:
    """
    Compara placeholders do template com as variáveis fornecidas.
    Case-insensitive para chaves (ex: 'cliente-nome' satisfaz '[[CLIENTE-NOME]]').
    """
    # Normaliza chaves fornecidas para uppercase sem traços
    norm_provided = {
        re.sub(r'[^A-Z0-9]', '', k.upper()): v
        for k, v in provided_vars.items()
    }

    missing = []
    for ph in required_placeholders:
        norm_ph = re.sub(r'[^A-Z0-9]', '', ph.upper())
        if norm_ph not in norm_provided or not str(norm_provided[norm_ph]).strip():
            missing.append(ph)

    return len(missing) == 0, missing

def assert_no_leaked_placeholders(rendered_content: str) -> List[str]:
    """
    Verifica que nenhum [[PLACEHOLDER]] ou {{PLACEHOLDER}} sobreviveu à renderização.
    Retorna lista dos que sobreviveram (deve ser vazia).
    """
    bracket_leaks = re.findall(r'\[\[([A-Z0-9_-]+)\]\]', rendered_content)
    mustache_leaks = re.findall(r'\{\{([A-Z0-9_-]+)\}\}', rendered_content)
    return sorted(list(set(bracket_leaks + mustache_leaks)))
