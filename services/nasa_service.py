import requests
from config.settings import NASA_APOD_URL, REQUEST_TIMEOUT

def get_apod():
    try:
        response = requests.get(NASA_APOD_URL, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        return data if isinstance(data, dict) else {}
    except Exception:
        return {} 