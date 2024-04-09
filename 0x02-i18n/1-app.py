#!/usr/bin/env python3
"""A Flask application"""
from flask import Flask, render_template
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


@app.route('/', strict_slashes=False)
def index():
    """The Index route"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
