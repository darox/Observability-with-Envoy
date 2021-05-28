# Observability with Envoy

A sandbox environment to play around with the three pillars of observability and traceID correlation. The observability completely takes place in Envoy, no code instrumentation in the Python Flask apps. This project also includes some Service Level Indicator recording rules in Prometheus and a dashboard for it in Grafana. Everything is preconfigured and should work out of the box. 


The overall request flow looks like this:
![Alt text](images/Overview.png?raw=true "Architecture")

The environment consists of:
- Grafana
- Blackbox Exporter
- Prometheus
- Loki
- Promtail
- Zipkin
- Python Flask apps
- Envoy proxy

In a real world scenario you would typically run this kind of environment on k8s and inject the Envoy proxy into the pod However, I wanted to keep it simple. That's why I have chosen Docker-Compose over k8s. 

![Alt text](images/requestflow.png?raw=true "Request flow")

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
 - :9115 (Blackbox Exporter Debug)
 - :80 (Python Flask App)

Useful commands:
- docker-compose ps (to list containers)
- docker-compose logs (to show log of containers)
- docker-compose down (to stop the stack)
- docker-compose images (to show the used images)
- docker-compose up -d --build (to rebuild the stack and detach from terminal)


## Future ideas

I plan adding additional features to this sandbox project, as they come available and whenever I have time to add them. I am thinking of:

- Exemplars 
- Add traceID to error log of Python Flask apps. 

## Tested on

The stack was tested on:
- Ubuntu 20.04 x86
- Windows x86
- MacOS ARM64


### Warning

Do not run this stack at all in a production environment. It's not secured at all. 


