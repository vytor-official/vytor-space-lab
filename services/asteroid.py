import requests

NASA_KEY = "YOUR_NASA_API_KEY"
URL = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={NASA_KEY}"

def get_asteroids():
    try:
        r = requests.get(URL, timeout=10)
        data = r.json()

        near = data.get("near_earth_objects", {})
        first_day = list(near.values())[0]
        return len(first_day)

    except:
        return 0
