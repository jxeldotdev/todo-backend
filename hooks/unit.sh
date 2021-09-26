#!/bin/bash

echo "Running unit tests"

docker-compose run up -d db
docker-compose run --rm app migrate
docker-compose run --rm app test