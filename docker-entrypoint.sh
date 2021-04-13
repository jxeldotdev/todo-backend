#!/bin/sh

for var in POSTGRES_USER POSTGRES_PASSWORD POSTGRES_DB POSTGRES_HOST ; do
    if ! env | grep -c "$var" > /dev/null; then echo "Required variable $var is unset" 1>&2; exit 1; fi
done

case "$@" in 
    web)
        cd /home/todoapp/src/
        python run.py
        ;;
    migrate)
        echo "command $@ not implemented yet" 1>&2
        exit 1
        ;;
    test)
        echo "command $@ not implemented yet" 1>&2
        exit 1
        ;;
    *)
        echo "Unknown command specified - command was $@" 1>&2
        echo "Available commands: web, migrate, test" 1>&2
        exit 1 
        ;;
esac