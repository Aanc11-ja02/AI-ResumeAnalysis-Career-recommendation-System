from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[
        DataRequired(message="Please provide your email address."),
        Email(message="Please enter a valid email address.", check_deliverability=False)
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message="Please enter your password.")
    ])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    full_name = StringField('Full Name', validators=[
        DataRequired(message="Please enter your full name."),
        Length(min=2, max=100, message="Name must be between 2 and 100 characters.")
    ])
    email = StringField('Email Address', validators=[
        DataRequired(message="Please enter your email address."),
        Email(message="Please enter a valid email address.", check_deliverability=False)
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message="Please provide a password."),
        Length(min=6, message="Password must be at least 6 characters long.")
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(message="Please confirm your password."),
        EqualTo('password', message="Passwords must match.")
    ])
    submit = SubmitField('Create Account')


class ProfileForm(FlaskForm):
    full_name = StringField('Full Name', validators=[
        DataRequired(message="Please enter your full name."),
        Length(min=2, max=100, message="Name must be between 2 and 100 characters.")
    ])
    email = StringField('Email Address', validators=[
        DataRequired(message="Please enter your email address."),
        Email(message="Please enter a valid email address.", check_deliverability=False)
    ])
    submit = SubmitField('Update Profile')


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[
        DataRequired(message="Current password is required.")
    ])
    new_password = PasswordField('New Password', validators=[
        DataRequired(message="New password is required."),
        Length(min=6, message="New password must be at least 6 characters long.")
    ])
    confirm_new_password = PasswordField('Confirm New Password', validators=[
        DataRequired(message="Please confirm your new password."),
        EqualTo('new_password', message="New passwords must match.")
    ])
    submit = SubmitField('Update Password')


class ResumeUploadForm(FlaskForm):
    resume = FileField('Upload Resume (PDF or DOCX, max 5 MB)', validators=[
        FileRequired(message="Please select a resume file to analyze."),
        FileAllowed(['pdf', 'docx'], message="Only PDF and DOCX files are allowed.")
    ])
    submit = SubmitField('Analyze Resume with AI')
