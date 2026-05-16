import requests

URL = "http://api.open-notify.org/iss-now.json"

def get_iss_position():
    try:
        r = requests.get(URL, timeout=10)
        data = r.json()
        return data.get("iss_position", {})
    except:
        return {}
