#!/usr/bin/env python3
""" Flask application module
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ Flask app configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Gets a client's locale/region"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def home():
    """ The Home route
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
