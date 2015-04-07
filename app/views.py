from app import app
from flask import render_template

@app.route('/')
def get_books():
    return render_template('books.html')
