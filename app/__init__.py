from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
# Research what needs to go here re 'from_object'.
#app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/books"
db = SQLAlchemy(app)

from app import views, models
