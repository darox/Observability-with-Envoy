# Observability with Envoy

A sandbox environment to play around with the three pillars of observability and traceID correlation. The observability completely happens in Envoy, no code instrumentation in the Flask Pythonn apps. 

![Alt text](images/Overview.png?raw=true "Architecture")

The environment consists of:
- Grafana
- Blackbox Exporter
- Prometheus
- Loki
- Promtail
- Zipkin
- Flask Python Apps
- Envoy proxy

In a real world scenario you would typically run this kind of environment on k8s. However, I wanted to keep it simple. That's why I have chosen Docker-Compose to spin up the environment.

## Prerequisites
- Docker Desktop https://www.docker.com/products/docker-desktop
- Git
- Docker-Compose https://docs.docker.com/compose/install/
- Internet connectivity
- Time 😉

## Setup environment
1. Clone repo "git clone https://github.com/darox/Observability-with-Envoy"
2. Cd into folder "cd Observability-with-Envoy"
3. Start stack "docker-compose up" (to detach from terminal, just add –d flag)
4. Open webbrowser and go to 127:0.0.1 
 - :3000 (Grafana)
 - :9090 (Prometheus Server UI)
 - :9115 Blackbox Exporter Debug

Useful commands:
- docker-compose ps (to list containers)
- docker-compose logs (to show log of containers)
- docker-compose down (to stop the stack)
- docker-compose images (to show the used images)
- docker-compose up -d --build (to rebuild the stack and detach from terminal)


