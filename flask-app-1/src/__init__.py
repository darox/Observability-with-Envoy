from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


TRACE_HEADERS_TO_PROPAGATE = [
    "X-Ot-Span-Context",
    "X-Request-Id",

    # Zipkin headers
    "X-B3-TraceId",
    "X-B3-SpanId",
    "X-B3-ParentSpanId",
    "X-B3-Sampled",
    "X-B3-Flags",

    "uber-trace-id",
]

@app.route('/', methods=["GET"])
def index():
    headers = {}
    for header in TRACE_HEADERS_TO_PROPAGATE:
        if header in request.headers:
            headers[header] = request.headers[header]
    try:
        response = requests.get("http://envoy-sidecar-1:9090/api/v1/status", headers=headers)
    
        return jsonify(response.json())
    except:
        return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)