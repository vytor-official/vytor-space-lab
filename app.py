from flask import Flask, jsonify, render_template
from config.settings import APP_NAME
from core.engine import get_dashboard_data
from services.iss_service import get_iss_position

app = Flask(__name__)

@app.route("/")
def home():
    data = get_dashboard_data()
    return render_template("index.html", app_name=APP_NAME, **data)

@app.route("/api/iss")
def iss_api():
    return jsonify(get_iss_position())

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)