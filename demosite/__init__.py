from demosite import app
import logging.config
import os


def get_app(config=None, logging_config=None):
    """
    Return a configured WSGI application.

    Keyword arguments:
    config -- absolute path a config file
    logging_config -- absolute path to a python logging config
    """

    if config is None:
        config = os.path.join(app.root_path, '../etc/config.cfg')

    app.config.from_pyfile(config)

    if logging_config is not None:
        app.logger
        logging.config.fileConfig(logging_config)

    return app


def development_server():
    """
    Run the development server
    """
    get_app().run(debug=True)
