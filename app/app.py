from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/books"
#app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():
    return "testy print statement wow"

@app.route('/books')
def get_books():
    return "this is where a book live!"



class Book(db.Model):
  __tablename__ = 'books'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String())
  author = db.Column(db.String())

  def __init__(self, title, author):
    self.title = title
    self.author = author

  def __repr__(self):
    return '<id {}>'.format(self.id)



if __name__ == '__main__':
    app.run()