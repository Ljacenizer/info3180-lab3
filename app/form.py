from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import InputRequired, Email



class ContactForm(FlaskForm):
    
    required = StringField("(Required)")
    name = StringField("Name",validators=[InputRequired()])
    namemsg = StringField("Please enter your full name")

    email = StringField("Email",validators=[InputRequired(),Email()])
    emailmsg = StringField("Please enter your e-mail address")

    subject = StringField("Subject",validators=[InputRequired()])
    subjectmsg = StringField("Please enter the subject for your message")

    message = TextAreaField('Message', validators=[InputRequired()])
    messagemsg = StringField("Please enter the message you would like to send")
    submit = SubmitField("Send")

