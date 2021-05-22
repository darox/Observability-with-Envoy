from flask import Flask, request, render_template
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
    print(headers)            
    
    try:
        response = requests.get("http://envoy-sidecar-1:9090/api/v1/status", headers=headers)
        print(response.json())

        return render_template("index.html", response=response), 200

    except AssertionError as e:
        return render_template("error.html"), 500
        print(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)