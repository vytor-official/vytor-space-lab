import requests

NASA_KEY = "YOUR_NASA_API_KEY"
URL = f"https://api.nasa.gov/planetary/apod?api_key={NASA_KEY}"

def get_apod():
    try:
        r = requests.get(URL, timeout=10)
        return r.json()
    except:
        return {}
