from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    """
    Index route handler
    """
    app.logger.debug('Rendering Index')
    return render_template('index.html', tagline=app.config["TAGLINE"])
