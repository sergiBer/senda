#!/usr/bin/env python3
"""Comprueba que cada acceptance criterion de una spec tiene al menos un test (HAR-06).

Para cada `specs/NNN-nombre/spec.md` busca los criterios `### AC-NN` y exige que
la etiqueta `NNN/AC-NN` aparezca en algún fichero de test del repo, por ejemplo
como comentario `# 001/AC-01` (Python) o `// 001/AC-01` (TypeScript).

- Specs con estado "hecha": un AC sin test es un error (el CI falla).
- Specs "en curso": se avisa de los AC pendientes, sin fallar.
- El resto de estados (borrador, en revisión, aprobada) no se comprueban.

Uso: python scripts/check_ac.py [raíz-del-repo]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

AC_HEADING = re.compile(r"^###\s+(AC-\d{2,})\b", re.MULTILINE)
ESTADO = re.compile(r"^>\s*Estado:\s*(.+)$", re.MULTILINE | re.IGNORECASE)
SPEC_DIR = re.compile(r"^(\d{3})-")
TEST_GLOBS = (
    "backend/**/test_*.py",
    "backend/**/*_test.py",
    "frontend/**/*.test.ts",
    "frontend/**/*.test.tsx",
    "frontend/**/*.spec.ts",
    "frontend/**/*.spec.tsx",
    "e2e/**/*.ts",
)
EXCLUIR = ("node_modules", ".venv", "dist")


def leer_tests(raiz: Path) -> str:
    textos = []
    for patron in TEST_GLOBS:
        for f in raiz.glob(patron):
            if any(parte in EXCLUIR for parte in f.parts):
                continue
            textos.append(f.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(textos)


def estado_de(spec: str) -> str:
    m = ESTADO.search(spec)
    return m.group(1).strip().lower() if m else ""


def main() -> int:
    raiz = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    tests = leer_tests(raiz)
    errores, avisos = [], []

    for spec_md in sorted((raiz / "specs").glob("*/spec.md")):
        m = SPEC_DIR.match(spec_md.parent.name)
        if not m:  # _plantillas u otras carpetas
            continue
        num = m.group(1)
        texto = spec_md.read_text(encoding="utf-8")
        estado = estado_de(texto)
        if estado not in ("hecha", "en curso"):
            continue
        acs = AC_HEADING.findall(texto)
        if not acs:
            errores.append(f"{spec_md.parent.name}: no tiene acceptance criteria (### AC-NN)")
            continue
        sin_test = [ac for ac in acs if f"{num}/{ac}" not in tests]
        destino = errores if estado == "hecha" else avisos
        for ac in sin_test:
            destino.append(f"{spec_md.parent.name}: {num}/{ac} sin test")
        cubiertos = len(acs) - len(sin_test)
        print(f"{spec_md.parent.name} [{estado}]: {cubiertos}/{len(acs)} AC con test")

    for a in avisos:
        print(f"AVISO  {a}")
    for e in errores:
        print(f"ERROR  {e}")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
