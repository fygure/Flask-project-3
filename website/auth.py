# Login, Logout, Signup routes live here.
# Blueprint - Allows for views to be declared here and defined in another place.
from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign-up</p>"