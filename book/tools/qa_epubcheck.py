#!/usr/bin/env python3
"""Run the official EPUBCheck engine, with results bound to the export hash.

Requires PyPI epubcheck==5.3.0 and jdk4py (see bootstrap.sh).
A missing validator is a failure, not a silently skipped release check.
"""
from pathlib import Path
import hashlib
import json
import sys
ROOT = Path(__file__).resolve().parents[2]
try:
    import epubcheck.const as constants
    import jdk4py
    from epubcheck import EpubCheck
except ImportError:
    sys.exit('Official EPUBCheck unavailable: run bash book/tools/bootstrap.sh')
constants.JAVA = str(jdk4py.JAVA_HOME / 'bin/java')
file = ROOT / 'Master-Speaking.epub'
result = EpubCheck(str(file))
report = {'sha256': hashlib.sha256(file.read_bytes()).hexdigest(),
          'valid': result.valid, 'returncode': result._returncode,
          'engine_report': result.result_data}
(ROOT / 'book/artifacts/epubcheck-official.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({'valid': result.valid, 'checker': result.result_data.get('checker'),
                  'messages': result.result_data.get('messages')}, indent=2))
sys.exit(0 if result.valid else 1)
