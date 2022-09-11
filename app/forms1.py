from signal import default_int_handler
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange


class MessageForm(FlaskForm):
    '''name = StringField('Name: ')#, validators=[DataRequired()])
    email = StringField('Email: ')#, validators=[Email()])
    message = TextAreaField('Message: ')#, validators=[DataRequired()])'''
    submit = SubmitField('Submit')
    course = SelectField('Выбери сторону света', choices=[('0,1', 'Север'), ('1,0', 'Восток'), ('0,-1', 'Юг'), ('-1,0', 'Запад')])
    count_steps = IntegerField('На сколько шагов хотите продвинуться', 
                              [NumberRange(min=1, max=3, message="Вы не можете совершить меньше 1 шага и больше 3 шагов")],default = 1)
    