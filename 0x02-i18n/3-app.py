#!/usr/bin/env python3
"""
0x02. i18n
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """The configuration class for the application."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def main() -> str:
    """A basic flask method."""
    return render_template("3-index.html")


@babel.localeselector
def get_locale() -> str:
    """Determine which locale to use based on user's request header."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")
