#!/usr/bin/env python3
"""
0x02. i18n
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from datetime import datetime

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
    current_time = get_current_time()
    return render_template(
        "index.html", logged_in_as=user, current_time_is=current_time
    )


@babel.localeselector
def get_locale():
    """Determine which locale to use based on user's request header."""
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


@babel.timezoneselector
def get_timezone():
    """A method to determine the timezone of the current user."""
    if "timezone" in request.args:
        timezone = request.args.get("timezone")
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if hasattr(g, "user") and g.user and "timezone" in g.user:
        timezone = g.user["timezone"]
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return "UTC"


def get_current_time():
    """Get the current time in the user's timezone."""
    user_timezone = get_timezone()
    current_time = datetime.now(pytz.timezone(user_timezone))
    return current_time.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")
