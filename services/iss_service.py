import requests
from datetime import datetime, timezone
from config.settings import ISS_POSITION_URL, REQUEST_TIMEOUT

def get_iss_position():
    try:
        response = requests.get(ISS_POSITION_URL, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        position = data.get("iss_position", {})

        return {
            "latitude": str(position.get("latitude", "Unknown")),
            "longitude": str(position.get("longitude", "Unknown")),
            "timestamp": datetime.now(timezone.utc).strftime("%H:%M:%S UTC")
        }

    except Exception:
        return {
            "latitude": "Unknown",
            "longitude": "Unknown",
            "timestamp": "Unavailable"
        }