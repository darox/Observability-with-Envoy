from flask import Flask, request, render_template
import requests, json_logging, logging

app = Flask(__name__)

json_logging.init_flask(enable_json=True)
logger = logging.getLogger("flask-app-1")
logger.setLevel(logging.ERROR)
handler = logging.handlers.RotatingFileHandler(filename='/log/error.log', maxBytes=5000000, backupCount=10)
logger.addHandler(handler)


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
    print(headers)   
    print(headers['X-B3-TraceId'])      
    
    try:
        response = requests.get("http://envoy-sidecar-1:9090/api/v1/status", headers=headers)

        return render_template("index.html", response=response.json()), 200

    except AssertionError as e:
        message = str(e)
        traceid = headers['X-B3-TraceId']
        logger.error(message, extra={'props': {'trace_id': traceid}})
        return 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)