from flask import Flask, render_template
import requests

app = Flask(__name__)

NASA_API = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"


@app.route("/")
def home():
    try:
        response = requests.get(NASA_API, timeout=10)
        data = response.json()

        if "title" not in data:
            return f"""
            <h1>⚠️ NASA API Error</h1>
            <pre>{data}</pre>
            """

        return render_template(
            "index.html",
            title=data.get("title", "No Title"),
            image=data.get("url", ""),
            explanation=data.get("explanation", "No explanation available")
        )

    except Exception as e:
        return f"""
        <h1>⚠️ Server Error</h1>
        <pre>{str(e)}</pre>
        """


if __name__ == "__main__":
    app.run(debug=True)
