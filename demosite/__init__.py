from demosite import app
import logging.config
import os

# Load build configuration to
build_config = os.path.join(app.root_path, '/etc/build.cfg')
app.config.from_pyfile(build_config)

# Load application configuration
app.config.from_pyfile(app.config["CONFIG"])

# Load logging configuration
if "LOGGING" in app.config:
    logging.config.fileConfig(app.config["LOGGING"])

def development_server():
    app.run(debug=True)
