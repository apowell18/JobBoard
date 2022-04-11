from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, URLField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Optional, URL, EqualTo


class RegisterJobSeekerForm(FlaskForm):
    # job seekers can use a display name or real name
    firstName = StringField('First Name', validators=[DataRequired(), Length(min=1)])
    lastName = StringField('Last Name', validators=[DataRequired(), Length(min=1)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=8),EqualTo('password')])
    email = EmailField('Email', validators=[DataRequired(), Email()]) #validate email

    submit = SubmitField("Register User")
    #phone number
    #resume = FileField()
    #Highest level of Education
    #Job History
    #Desired Salary #hourly/yearly
    #Desired Job Title
    #Desired Location
    #Additional Links



class RegisterCompanyForm(FlaskForm):
    # display is company name
    companyName = StringField('Company Name', validators=[DataRequired(), Length(min=1)])
    site = URLField('Website', validators=[DataRequired(), URL()])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=8), EqualTo(password)])
    email = EmailField('Email', validators=[DataRequired(), Email()])  # validate email

    #business category i.e. Finance, Oil, Medical
    #mission statemet


class LoginForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    email = EmailField('Email', validators=[DataRequired(), Email()])  # validate email
    remeber = BooleanField('Remember Login')
    submit = SubmitField("Login User")

#class RegistrationForm(FlaskForm):
  #  val = 0
  #  if(val == 1):
   #     RegisterCompany(FlaskForm)
    #else:
     #   RegisterJobSeeker(FlaskForm)
    #submit = SubmitField('Register')