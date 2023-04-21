from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    # email. password, submit_button
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()
    
class DroneForm(FlaskForm):
    name = StringField('Name')
    description = StringField('Description')
    price = DecimalField('Price', places=2) # type: ignore
    camera_quality = StringField('Camera Quality')
    flight_time = StringField('Flight Time')
    max_speed = StringField('Max Speed')
    dimensions = StringField('Dimensions')
    weight = StringField('Weight')
    cost_of_production = DecimalField('Cost of Production', places=2) # type: ignore
    series = StringField('Series')
    random_joke = StringField('Random Joke')
    submit_button = SubmitField()