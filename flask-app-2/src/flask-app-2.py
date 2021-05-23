from flask import Flask, jsonify, request
import requests, json

app = Flask(__name__)

@app.route('/api/v1/status', methods=["GET"])
def serve_api():

    x =  {
        "listedBooks": [
            {
                "id": 1, 
                "title": "Absalom, Absalom!", 
                "author": "William Faulkner", 
                "year": 1936
            },
            {
                "id": 2, 
                "title": "A time to kill", 
                "author": "John Grisham", 
                "year": 1989
            }
        ]
    }

    return jsonify(x)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)