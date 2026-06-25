import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, jsonify
from dashboard.store import get_all_reviews, get_stats

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("dashboard.html")


@app.route("/api/reviews")
def reviews():
    return jsonify(get_all_reviews())


@app.route("/api/stats")
def stats():
    return jsonify(get_stats())


if __name__ == "__main__":
    port = int(os.getenv("DASHBOARD_PORT", 8080))
    print(f"Dashboard running on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)