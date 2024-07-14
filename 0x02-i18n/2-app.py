#!/usr/bin/env python3
""" Module for the basic flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ Configuration class for the Flask app
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
    """ Function to determine the best match with the supported languages
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def home():
    """ Function to render the home page
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0/0.0.0", port="5000")
