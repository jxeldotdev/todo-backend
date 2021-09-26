#!/bin/bash

echo "Updating packages"
pipenv sync
echo "Updating requirements.txt"
pipenv run pip freeze > requirements.txt
