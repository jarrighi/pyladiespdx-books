from app import app, db, models
from flask import render_template

@app.route('/')
def get_books():
    books = []

    query = db.session.query(models.Book)
    for book in query:
        book_dict = {}
        book_dict["title"] = book.title
        book_dict["author"] = book.author
        books.append(book_dict)
    return render_template('books.html', books=books)

@app.route('/books/<book>')
def book_page(book):
    
    # The following data should eventually get passed into the page
    # 
    # Title and Author of the book
    # Who has the book
    # Links to information about the book
    # tags that describe the book
    # butts
    # button to request the book
    book_details = {'title': 'python book', 'author': 'pythonista', 
                    'possessor': 'pyltergeist'}
    return render_template('book_detail.html', details=book_details)
