# i18n - Internationalization and Localization in Flask

Welcome to our journey into the world of internationalization and localization with Flask! 🌍✨ In this README, we'll explore how to make our Flask applications accessible to users from different linguistic backgrounds by learning how to parametrize Flask templates, infer the correct locale, and localize timestamps.

## Parametrizing Flask Templates for Different Languages

As software engineers, we understand the importance of building applications that cater to diverse audiences. With Flask, we can easily parametrize our templates to display content in different languages. Let's dive into a simple example:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Let's assume 'lang' is a parameter indicating the desired language
    lang = request.args.get('lang', 'en')
    # Render the template with the appropriate language parameter
    return render_template('index.html', lang=lang)

if __name__ == '__main__':
    app.run(debug=True)
```

In our template `index.html`, we can use the `lang` parameter to display content dynamically based on the selected language:

```html
<!DOCTYPE html>
<html lang="{{ lang }}">
<head>
    <meta charset="UTF-8">
    <title>i18n Demo</title>
</head>
<body>
    {% if lang == 'en' %}
        <h1>Hello!</h1>
    {% elif lang == 'fr' %}
        <h1>Bonjour !</h1>
    {% endif %}
</body>
</html>
```

By utilizing URL parameters like `?lang=en` or `?lang=fr`, we can seamlessly switch between languages, providing a personalized experience for our users.

## Inferring the Correct Locale

As passionate learners, we strive to make our applications intuitive and user-friendly. To achieve this, we can infer the correct locale based on various factors such as URL parameters, user settings, or request headers. Let's explore an example of inferring locale from URL parameters:

```python
from flask import Flask, request, g

app = Flask(__name__)

@app.before_request
def before_request():
    # Inferring locale from URL parameters
    g.locale = request.args.get('lang', 'en')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

By extracting the language parameter from the URL using `request.args.get('lang', 'en')`, we can set the locale for the current request, ensuring that content is displayed in the appropriate language.

## Localizing Timestamps

Timestamps are essential elements in many applications, and localizing them adds a personal touch for users worldwide. Let's see how we can localize timestamps using Flask-Moment:

```python
from flask import Flask, render_template
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
moment = Moment(app)

@app.route('/')
def index():
    # Get current timestamp
    now = datetime.utcnow()
    return render_template('index.html', now=now)

if __name__ == '__main__':
    app.run(debug=True)
```

In our template, we can use Flask-Moment's `moment` filter to localize the timestamp:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>i18n Demo</title>
    <script src="//cdnjs.cloudflare.com/ajax/libs/moment.js/2.29.1/moment.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/moment.js/2.29.1/locale/{{ g.locale }}.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/moment-timezone/0.5.38/moment-timezone-with-data.min.js"></script>
</head>
<body>
    <p>Current time: {{ now|moment('LLLL') }}</p>
</body>
</html>
```

By including the appropriate locale file and using the `moment` filter with the desired format ('LLLL' for full date and time), we can localize the timestamp based on the user's preferred language.

Congratulations, fellow software engineers! 🎉 We've now embarked on an exciting journey into the realm of internationalization and localization with Flask. Let's keep exploring, experimenting, and building amazing multilingual applications! 🚀
