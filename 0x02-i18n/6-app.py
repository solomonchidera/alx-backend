#!/usr/bin/env python3
"""
0x02. i18n
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """The configuration class for the application."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def main():
    """The main method."""
    user = before_request()
    return render_template("6-index.html", logged_in_as=user)


@babel.localeselector
def get_locale():
    """Determine which locale to use based on user's request header ."""
    language = request.args.get("locale")
    if language and language in app.config["LANGUAGES"]:
        return language
    if (
        hasattr(g, "user")
        and g.user
        and "locale" in g.user
        and g.user["locale"] in app.config["LANGUAGES"]
    ):
        return g.user["locale"]
    if request.accept_languages.best_match(app.config["LANGUAGES"]):
        return request.accept_languages.best_match(app.config["LANGUAGES"])
    return app.config["BABEL_DEFAULT_LOCALE"]


def get_user():
    """A method that verifies a user."""
    user_id = request.args.get("login_as")
    if user_id:
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """A method to be called before each request."""
    g.user = get_user()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")
