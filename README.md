## Application

A very simple Flask application.

## Development evironment

    virtualenv .
    ./bin/python setup.py develop

## Running development server

    ./bin/development-server

## Running gunicorn server

    ./bin/gunicorn "demosite:get_app()"
