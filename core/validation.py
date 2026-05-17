def safe_text(value, default="Unavailable"):
    if isinstance(value, str) and value.strip():
        return value
    return default

def safe_number(value, default=0):
    try:
        if isinstance(value, bool):
            return default
        return int(float(value))
    except (TypeError, ValueError):
        return default

def safe_dict(value):
    if isinstance(value, dict):
        return value
    return {}