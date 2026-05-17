def safe_text(value, default="Unavailable"):
    if isinstance(value, str) and value.strip():
        return value
    return default

def safe_number(value, default=0):
    if isinstance(value, (int, float)):
        return value
    return default 