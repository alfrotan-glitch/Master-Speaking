#!/usr/bin/env bash
# Bootstrap: reinstall python deps lost between sandbox sessions. Fast no-ops if present.
set -e
python3 -c "import docx, lxml, PIL, reportlab, fontTools, fitz, spellchecker" 2>/dev/null || \
  pip install --quiet --break-system-packages python-docx lxml reportlab fonttools brotli pymupdf pyspellchecker
python3 - <<'EOF'
import importlib
for m in ['docx','lxml','PIL','reportlab','fontTools','fitz','spellchecker']:
    importlib.import_module(m)
print("python deps OK")
EOF

# Official EPUBCheck 5.3.0 and a local Java runtime; packages stay outside Git.
python3 -c "import epubcheck, jdk4py" 2>/dev/null || \
  pip install --quiet --break-system-packages epubcheck==5.3.0 jdk4py
