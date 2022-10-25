# Login, Logout, Signup routes live here.
# Blueprint - Allows for views to be declared here and defined in another place.
from pydoc import render_doc
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logged Out</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")