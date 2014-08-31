from demosite import app
import logging.config
import os


# Load application configuration
config_path = os.environ.get("DEMOSITE_CONFIG_PATH")
if config_path is None:
    config_path = os.path.join(app.root_path, '../etc/config.cfg')
app.config.from_pyfile(config_path)

# Load logging configuration
logging_config = os.environ.get("DEMOSITE_LOGGING_CONFIG_PATH")
if logging_config is not None:
    logging.config.fileConfig(logging_config)


def development_server():
    app.run(debug=True)
