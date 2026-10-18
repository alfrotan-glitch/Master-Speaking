"""Reviewed image descriptions shared by the semantic book, Word and EPUB."""
from functools import lru_cache
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]


@lru_cache(maxsize=1)
def descriptions():
    record = json.loads((ROOT / 'book/master/image-descriptions.json').read_text())
    result = {}
    for entry in record['images']:
        path = ROOT / entry['path']
        if hashlib.sha256(path.read_bytes()).hexdigest() != entry['sha256']:
            raise ValueError(f'Image changed; review its description: {path.name}')
        if not entry['alt'].strip():
            raise ValueError(f'Image description is empty: {path.name}')
        for name in [entry['file'], *entry.get('aliases', {})]:
            if name in result:
                raise ValueError(f'Duplicate image description: {name}')
            result[name] = entry['alt']
        for name, digest in entry.get('aliases', {}).items():
            if hashlib.sha256((path.parent / name).read_bytes()).hexdigest() != digest:
                raise ValueError(f'Image alias changed; review its description: {name}')
    return result


def description_for(filename):
    name = Path(filename).name
    if name not in descriptions():
        raise ValueError(f'No reviewed image description: {name}')
    return descriptions()[name]
