# infra

Kubernetes related infrastructure and manifests for the application and it's basic configuration.
Currently only tested on Minikube.

`nginx.conf.template` is used in docker - the nginx conf in the configmap is slightly difference as since nginx and the api are in the same pod in k8s `localhost` can be used, but the name of the container must be used with docker-compose.

![Diagram](diagram.png)