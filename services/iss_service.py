import requests
from config.settings import ISS_POSITION_URL, REQUEST_TIMEOUT

def get_iss_position():
    try:
        response = requests.get(ISS_POSITION_URL, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        return data.get("iss_position", {})
    except Exception:
        return {} 