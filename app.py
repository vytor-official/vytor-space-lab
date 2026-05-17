from flask import Flask, jsonify, render_template
from core.engine import get_dashboard_data
from services.iss_service import get_iss_position

app = Flask(__name__)


@app.route("/")
def home():
    data = get_dashboard_data()
    return render_template("index.html", **data)


@app.route("/api/iss")
def iss_api():
    return jsonify(get_iss_position())


if __name__ == "__main__":
    app.run()