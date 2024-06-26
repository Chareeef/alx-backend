#!/usr/bin/env python3
"""A Flask application"""
from flask import Flask, render_template, request
from flask_babel import Babel

# Create the app
app = Flask(__name__)


class Config:
    """Flask app configuration class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Configure the app
app.config.from_object(Config)

# Set up Babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Choose the best language to serve among the supported ones"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """The Index route"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
