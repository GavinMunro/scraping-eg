#!/bin/bash

. venv/bin/activate
# flask db upgrade
# flask translate compile

exec flask run --host=0.0.0.0 --port=5000

