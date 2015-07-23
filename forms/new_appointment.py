from flask_wtf import Form
from wtforms import StringField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, Length

class NewAppointmentForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    phone_number = IntegerField('Phone number', validators=[DataRequired(), Length(min=6)])
    delta = IntegerField('Notification time', validators=[DataRequired()])
    time = DateTimeField('Appointment time', validators=[DataRequired()], format="%m-%d-%Y %I:%M%p")
    timezone = StringField('timezone', validators=[DataRequired()])
