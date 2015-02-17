from app import app
from flask import render_template

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
    # Need to figure out new lines... or just make a template
    stringy_books = "<br><br>".join(book_titles)
    return """this is where a book live!<br><br>

    {}

    """.format(stringy_books)
