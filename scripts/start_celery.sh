#!/bin/sh

export ENVIRONMENT=local
celery -A tasks worker -B --loglevel=info
