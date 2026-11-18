import os
import socket

import requests
from flask import Flask

app = Flask(__name__)

BACKEND_URL = os.environ.get("BACKEND_URL", "http://backend-service:80")


@app.route("/")
def index():
    try:
        r = requests.get(BACKEND_URL, timeout=3)
        backend_answer = r.text
    except requests.RequestException as exc:
        return f"FRONTEND ({socket.gethostname()}): backend unavailable: {exc}", 502
    return f"FRONTEND pod: {socket.gethostname()} | backend answered: {backend_answer}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)