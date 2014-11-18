from flask import render_template, request
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "testy print statement wow"

@app.route('/books')
def get_books():
    return "this is where a book live!"
