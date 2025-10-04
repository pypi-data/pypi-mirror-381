def _is_likely_utf16le(raw: bytes) -> bool:
    if not raw:
        return False
    if raw.startswith(b'\xff\xfe'):
        return True
    nul_ratio = raw.count(b'\x00') / max(1, len(raw))
    return nul_ratio > 0.2

def _smart_decode(raw: bytes) -> str:
    if not raw:
        return ""
    try:
        if _is_likely_utf16le(raw):
            return raw.decode('utf-16-le').strip()
        return raw.decode('utf-8').strip()
    except UnicodeDecodeError:
        for enc in ('utf-16-le', 'utf-16-be', 'cp1252', 'latin1'):
            try:
                return raw.decode(enc).strip()
            except UnicodeDecodeError:
                continue
        return raw.decode('utf-8', errors='replace').strip()