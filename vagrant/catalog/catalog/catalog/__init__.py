__author__ = 'erik'

from flask import Flask
app = Flask(__name__, static_url_path='/static')

from catalog import views
from catalog import auth_routes
