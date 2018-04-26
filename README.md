# Flask-WTF-Decorators [![Build Status](https://travis-ci.org/simpleapples/flask-wtf-decorators.svg?branch=master)](https://travis-ci.org/simpleapples/flask-wtf-decorators) [![Coverage Status](https://coveralls.io/repos/github/simpleapples/flask-wtf-decorators/badge.svg?branch=master)](https://coveralls.io/github/simpleapples/flask-wtf-decorators?branch=master)

Using decorators to validate form.

# Installation

Using pip

`pip install flask-wtf-decorators`

Using Pipenv

`pipenv install flask-wtf-decorators`

# Usage

Flask-WTF-Decorators is easy to use. You can define a view that requires validation.

```python
from flask-wtf-decorators import FormValidator

form_validator = FormValidator()

@form_validator.validate_form(TestForm)
@app.route('/', methods=['GET', 'POST'])
def index(form):
    pass
```

You can tell Flask-WTF-Decorators what to do when a form is illegal. To do this you should provide a callback for `error_handler`.

```python
@form_validator.error_handler
def error_handler(errors):
    return jsonify({'errors': errors}), 400
```

# Test

`python -m unittest discover -s tests`

# Contributing

Please submit a pull request to contribute.

# License

This project is licensed under the MIT License.
