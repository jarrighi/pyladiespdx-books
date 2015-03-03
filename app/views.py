from app import app
from flask import render_template
from models import Book

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/books')
def get_books():
    the_books = Book.query.all()
    book_titles = []
    for book in the_books:
      book_info = "{} by {}".format(book.title, book.author)
      book_titles.append(book_info) 
    return render_template('books.html', books=book_titles)
