import requests
from config.settings import NASA_ASTEROID_URL, REQUEST_TIMEOUT

def get_asteroids():
    try:
        response = requests.get(NASA_ASTEROID_URL, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        near_objects = data.get("near_earth_objects", {})
        if not near_objects:
            return {"date": "Unknown", "count": 0}
        first_day = next(iter(near_objects))
        objects = near_objects.get(first_day, [])
        return {"date": first_day, "count": len(objects)}
    except Exception:
        return {"date": "Unknown", "count": 0} 