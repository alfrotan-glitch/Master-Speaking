#!/usr/bin/env bash
# Bootstrap: reinstall python deps lost between sandbox sessions. Fast no-ops if present.
set -e
python3 -c "import docx, reportlab, fontTools, fitz" 2>/dev/null || \
  pip install --quiet --break-system-packages python-docx lxml reportlab fonttools brotli pymupdf
python3 - <<'EOF'
import importlib
for m in ['docx','lxml','reportlab','fontTools','fitz']:
    importlib.import_module(m)
print("python deps OK")
EOF
