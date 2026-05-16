from flask import Flask, render_template
import requests

app = Flask(__name__)

NASA_KEY = "YOUR_NASA_API_KEY"

APOD_URL = f"https://api.nasa.gov/planetary/apod?api_key={NASA_KEY}"
ISS_URL = "http://api.open-notify.org/iss-now.json"
ASTEROID_URL = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={NASA_KEY}"

@app.route("/")
def home():
    apod = requests.get(APOD_URL).json()
    iss = requests.get(ISS_URL).json()
    asteroid = requests.get(ASTEROID_URL).json()

    if "title" not in apod:
        return {"error": "APOD API failed"}

    iss_pos = iss.get("iss_position", {})
    asteroid_count = len(list(asteroid.get("near_earth_objects", {}).values())[0])

    return render_template(
        "index.html",
        title=apod.get("title"),
        image=apod.get("url"),
        explanation=apod.get("explanation"),
        lat=iss_pos.get("latitude"),
        lon=iss_pos.get("longitude"),
        asteroids=asteroid_count
    )

if __name__ == "__main__":
    app.run(debug=True)
