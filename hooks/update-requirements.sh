#!/bin/bash

echo "Running $BASH_SOURCE"
FILE="/tmp/pipenv-pip-freeze.txt"
pipenv run pip freeze > $FILE

if [ (( $(cat $FILE | wc -l ) > 15 )) ]; then
    mv $FILE requirements.txt
fi