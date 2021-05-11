from flask import Flask, jsonify, request
import requests, json

app = Flask(__name__)

@app.route('/api/v1/status', methods=["GET"])
def serve_api():

    x =  '{"NetworkStatus": "UP"}'
    y = json.loads(x)

    return jsonify(y)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)