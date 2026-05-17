from flask import Flask, render_template
from core.engine import get_dashboard_data

app = Flask(__name__)

@app.route("/")
def home():
    data = get_dashboard_data()
    return render_template("index.html", **data)

if __name__ == "__main__":
    app.run(debug=True) 