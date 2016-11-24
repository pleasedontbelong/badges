#!/bin/sh

if [ "$1" = "--dev" ]; then
    pip install -r requirements/dev.txt
    if [ ! -f ./settings/local.default.py ]; then
        cp ./settings/local.default.py ./settings/local.py
    fi
elif [ "$1" = "--prod" ]; then
    pip install -r requirements/prod.txt
else
    echo "argument needed (--dev, --prod)"
fi
