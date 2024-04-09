#!/usr/bin/env python3
"""A Flask application"""
from flask import Flask, render_template

# Create the app
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """The Index route"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
