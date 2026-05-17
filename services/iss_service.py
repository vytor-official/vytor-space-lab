import requests
from datetime import datetime
from config.settings import ISS_POSITION_URL, REQUEST_TIMEOUT


def get_iss_position():
    try:
        response = requests.get(ISS_POSITION_URL, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()

        data = response.json()
        position = data.get("iss_position", {})

        return {
            "latitude": position.get("latitude", "Unknown"),
            "longitude": position.get("longitude", "Unknown"),
            "timestamp": datetime.utcnow().strftime("%H:%M:%S UTC")
        }

    except Exception:
        return {
            "latitude": "Unknown",
            "longitude": "Unknown",
            "timestamp": "Unavailable"
        }