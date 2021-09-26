#!/bin/bash

echo "Running $BASH_SOURCE"

docker-compose run --rm --entrypoint sh app -c 'pip install flake8; flake8 -v ./'