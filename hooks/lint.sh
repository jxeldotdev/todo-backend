#!/bin/bash

echo "Running flake8"

docker-compose run --rm --entrypoint sh app -c 'pip install flake8 ; flake8 -v ./'

