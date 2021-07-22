#!/usr/bin/env bash

exec ./wait-for-it.sh $POSTGRES_APP_HOST:$POSTGRES_APP_PORT -- "$@"
