# Blueprint - Allows for views to be declared here and defined in another place
# Register these blueprints in the __init__.py
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")