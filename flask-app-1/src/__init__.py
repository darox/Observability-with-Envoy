from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    try:
        return jsonify(requests.get("http://envoy-sidecar-flask-app-2/api/v1/status"))
    except:
        return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)