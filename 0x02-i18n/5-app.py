#!/usr/bin/env python3
"""A Flask application"""
from flask import Flask, g, render_template, request
from flask_babel import Babel
from typing import Dict, Union

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

# Set up Babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Choose the best language to serve among the supported ones
    or the one specified in 'locale' URL parameter if given and supported
    """
    # If we have 'locale' in the request arguments
    # and this language is supported, return it
    lang = request.args.get('locale')
    if lang and lang in app.config['LANGUAGES']:
        return lang

    # Return the default preference
    return request.accept_languages.best_match(app.config['LANGUAGES'])


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
    g.user = get_user()


@app.route('/')
def index():
    """The Index route"""
    return render_template('5-index.html', user=g.user)


if __name__ == '__main__':
    app.run()
