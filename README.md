<!-- PROJECT LOGO -->
<br />

  <h3 align="center">Joel's Todo App - Backend</h3>

  <p align="center">
    This is the REST API backend for my example todo list application, written in Python using the framework FastAPI.
    <br />
    It is (to be) deployed on Amazon EKS by a Helm chart using Terraform.
    <br />
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


## About The Project

This is an example project to deploy a python (Fast API) todo app on AWS EKS.

### Built With

* [FastAPI](https://github.com/tiangolo/fastapi)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [PostgreSQL](https://www.postgresql.org/)

## Getting Started

To get a **local** copy of the application up and running follow these steps.

### Prerequisites

* Docker (or Podman)
* Docker Images for 

```sh
docker pull jfreemxn/todo-backend:latest
docker pull jfreemxn/todo-frontend:latest

docker-compose up -d
```

## Usage


## Contributing

Unfortunately for this repository pull requests will not be merged into this projcet as it is a personal showcase.

<!-- ## Todo List

[x] Create a Backend API

[] Create Unit tests for API

[] Add logging to the application

[] Create a Helm chart for the application

[] Automate tests of App using CI

[] Create a seperate repo with Terraform configuration for EKS infrastructure

[] Automate deployment of application

[] Add monitoring to app with Prometheus -->
