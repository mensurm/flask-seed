
from wtforms import Form
from wtforms.fields import StringField
from wtforms.validators import DataRequired


class UserForm(Form):
    first_name = StringField('First name', [DataRequired(message='First name not specified')])
    last_name = StringField('Last name', [DataRequired(message='Last name not specified')])