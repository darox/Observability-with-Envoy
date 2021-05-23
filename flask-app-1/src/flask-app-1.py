from flask import Flask, request, render_template
import requests, json_logging, logging

app = Flask(__name__)

json_logging.init_flask(enable_json=True)
json_logging.init_request_instrument(app)

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
    
    logger = logging.getLogger("flask-app-1")
    logger.setLevel(logging.INFO)
    handler = logging.handlers.RotatingFileHandler(filename='/log/debug-flask-app-1.log', maxBytes=5000000, backupCount=10)
    logger.addHandler(handler)

    headers = {}
    for header in TRACE_HEADERS_TO_PROPAGATE:
        if header in request.headers:
            headers[header] = request.headers[header]    
    
    try:
        response = requests.get("http://envoy-sidecar-1:9090/api/v1/status", headers=headers)
        logger.info("This request was handeled successfully")
        return render_template("index.html", response=response.json()), 200

    except AssertionError as e:
        logger.error("This request has failed")
        return 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)