#!/bin/bash

echo "Running $BASH_SOURCE"

docker-compose run up -d db
docker-compose run --rm app migrate
docker-compose run --rm app test