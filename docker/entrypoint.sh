#!/bin/sh

echo "Starting docker service"

if test -z $1 ; then
    echo "The docker arg is empty"
    python
else
    echo "The docker args list is not empty: $@"
    exec "$@"
fi
