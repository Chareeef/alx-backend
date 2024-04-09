#!/usr/bin/env python3
"""A Flask application"""
from datetime import datetime
import flask
from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Dict, Union
import pytz
from pytz.exceptions import UnknownTimeZoneError

# Create the app
app = Flask(__name__)


class Config:
    """Flask app configuration class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Configure the app
app.config.from_object(Config)
app.url_map.strict_slashes = False


def get_locale() -> str:
    """Choose the best language to serve among the supported ones
    respecting this order of priority:

        1. Locale from URL parameters
        2. Locale from user settings
        3. Locale from request header
        4. Default locale
    """
    # URL parameters
    lang = request.args.get('locale')
    if lang and lang in app.config['LANGUAGES']:
        return lang

    # user settings
    if flask.g.user:
        return flask.g.user['locale']

    # request header
    lang = request.headers.get('locale')
    if lang and lang in app.config['LANGUAGES']:
        return lang

    # Default locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone() -> str:
    """Set the timezone respecting this order of priority:

        1. Locale from URL parameters
        2. Locale from user settings
        4. Default to UTC
    """
    # URL parameters
    tz = request.args.get('timezone')
    try:
        return pytz.timezone(tz)
    except UnknownTimeZoneError:
        pass

    # user settings
    if flask.g.user:
        try:
            return flask.g.user['timezone']
        except UnknownTimeZoneError:
            pass

    # Default timezone: UTC
    return pytz.utc


# Set up Babel
babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Return a user dictionary, or None if the ID
    cannot be found or if login_as was not passed
    """
    try:
        user_id = int(request.args.get('login_as'))
    except BaseException:
        return None

    return users.get(user_id)


@app.before_request
def before_request() -> None:
    """Should use get_user to find a user if any,
    and set it as a global on flask.g.user
    """
    flask.g.user = get_user()


@app.route('/')
def index():
    """The Index route"""
    current_time = datetime.now(get_timezone())
    locale = get_locale()

    if locale == 'en':
        current_time = current_time.strftime('%b %d, %Y, %I:%M:%S %p')
    if locale == 'fr':
        current_time = current_time.strftime('%d %b. %Y à %H:%M;%S')

    return render_template('index.html',
                           user=flask.g.user,
                           current_time=current_time)


if __name__ == '__main__':
    app.run()
