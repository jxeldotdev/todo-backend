#!/bin/bash
docker-compose up -d db; echo $?
docker-compose run --rm app migrate; echo $?
docker-compose run --rm app test; echo $?
