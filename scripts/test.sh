#!/bin/sh

flake8
python ./manage.py test --failfast
