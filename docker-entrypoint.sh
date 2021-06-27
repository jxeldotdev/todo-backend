#!/bin/sh

for var in POSTGRES_USER POSTGRES_PASSWORD POSTGRES_DB POSTGRES_HOST ; do
    if ! env | grep -c "$var" > /dev/null; then echo "Required variable $var is unset" 1>&2; exit 1; fi
done

cd /home/todoapp/src

case "$@" in 
    web)
        exec uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
        ;;
    migrate)
        exec alembic upgrade head
        ;;
    test)
        exec pytest -vvv
        ;;
    *)
        echo "Unknown command specified - command was $@" 1>&2
        echo "Available commands: web, migrate, test" 1>&2
        exit 1 
        ;;
esac