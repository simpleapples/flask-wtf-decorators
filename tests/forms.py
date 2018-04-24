from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import DataRequired
from wtforms.validators import NumberRange


class TestForm(FlaskForm):
    test_str = StringField(validators=[DataRequired()])
    test_int = IntegerField(validators=[NumberRange(min=10)])
