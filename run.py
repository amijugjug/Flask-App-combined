'''
from datetime import datetime
from flask import Flask, render_template,url_for,flash,redirect
# from form.py file we created importing 2 modules
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Secret key is needed to protect us against modifying cookies or forgery attacks
app.config['SECRET_KEY'] = '40f79cf957ac02384c847f9c9c213b41'
# Setting location of database setting URI for database which indicates where the database acctually is 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# sqlite:///site.db is relative path of DB
# Instance of SQLAlchemy
db=SQLAlchemy(app)
'''
from flask_blog import app
if __name__ == '__main__':
    app.run(debug=True)
