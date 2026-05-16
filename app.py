from flask import Flask, render_template
import requests

app = Flask(__name__

NASA_API = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

@app.route("/")
def home():

    response = requests.get(NASA_API)
    data = response.json()

    return render_template(
        "index.html",
        title=data["title"],
        image=data["url"],
        explanation=data["explanation"]
    )

if __name__ == "__main__":
    app.run(debug=True)
