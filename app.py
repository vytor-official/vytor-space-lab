from flask import Flask, render_template
from services.nasa import get_apod
from services.iss import get_iss_position
from services.asteroid import get_asteroids

app = Flask(__name__)

@app.route("/")
def home():
    apod = get_apod()
    iss = get_iss_position()
    asteroid = get_asteroids()

    return render_template(
        "index.html",
        title=apod.get("title"),
        image=apod.get("url"),
        explanation=apod.get("explanation"),
        lat=iss.get("latitude"),
        lon=iss.get("longitude"),
        asteroids=asteroid
    )

if __name__ == "__main__":
    app.run(debug=True)
