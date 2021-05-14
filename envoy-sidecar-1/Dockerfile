FROM envoyproxy/envoy:v1.18.2
RUN apt-get update && apt-get -q install -y \
    curl
CMD ["/usr/local/bin/envoy", "-c", "/etc/envoy/envoy.yaml", "--service-cluster", "envoy-sidecar-1"]