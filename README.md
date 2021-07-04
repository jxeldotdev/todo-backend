
# todo-backend

This is an example project to deploy a python (Fast API) todo app on AWS EKS.

## Installation

## Usage

```
docker-compose up -d db
docker-compose run --rm app migrate
docker-compose up -d app
```

## Contributing

Unfortunately for this repository pull requests will not be merged into this projcet as it is a personal showcase.

[] Add logging to the application

[] Create a Helm chart for the application

[] Automate tests of App using CI

[] Create a seperate repo with Terraform configuration for EKS infrastructure

[] Automate deployment of application

[] Add monitoring to app with Prometheus
