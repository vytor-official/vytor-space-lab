from flask import Flask, render_template
import requests

app = Flask(__name__)

NASA_API_KEY = "BURAYA_API_KEY_YAZMA_GELISTIRECEGIZ"

NASA_API = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"

@app.route("/")
def home():
    try:
        response = requests.get(NASA_API, timeout=10)
        data = response.json()

        if "title" not in data:
            return f"<pre>API Error: {data}</pre>"

        return render_template(
            "index.html",
            title=data.get("title"),
            image=data.get("url"),
            explanation=data.get("explanation")
        )

    except Exception as e:
        return f"<pre>Error: {e}</pre>"


if __name__ == "__main__":
    app.run(debug=True)
