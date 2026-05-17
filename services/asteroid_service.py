import requests
from config.settings import NASA_ASTEROID_URL, REQUEST_TIMEOUT

def get_asteroids():
    if not NASA_ASTEROID_URL:
        return {
            "date": "Unknown",
            "count": 0,
            "hazardous_count": 0
        }

    try:
        response = requests.get(NASA_ASTEROID_URL, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        near_objects = data.get("near_earth_objects", {})

        if not near_objects:
            return {
                "date": "Unknown",
                "count": 0,
                "hazardous_count": 0
            }

        first_day = next(iter(near_objects))
        objects = near_objects.get(first_day, [])
        hazardous_count = sum(
            1 for item in objects
            if item.get("is_potentially_hazardous_asteroid")
        )

        return {
            "date": first_day,
            "count": len(objects),
            "hazardous_count": hazardous_count
        }

    except Exception:
        return {
            "date": "Unknown",
            "count": 0,
            "hazardous_count": 0
        }