from app import app, db, models
from flask import render_template, redirect, url_for, request

@app.route('/')
def get_books():
    books = []

    query = db.session.query(models.Book)
    for book in query:
        book_dict = {}
        book_dict["title"] = book.title
        book_dict["author"] = book.author
        book_dict["id"] = book.id
        books.append(book_dict)
    return render_template('books.html', books=books)

@app.route('/books/<book>')
def book_page(book):

    the_book = models.Book.query.get(book)

    # The following data should eventually get passed into the page
    #
    # Title and Author of the book
    # Who has the book
    # Links to information about the book
    # tags that describe the book
    # butts
    # button to request the book
    book_details = {'title': the_book.title, 'author': the_book.author, 
                    'possessor': the_book.possessor}
    return render_template('book_detail.html', details=book_details)

@app.route('/books/new')
def new_book():
    return render_template('add_book.html')

@app.route('/books/add', methods=["POST"])
def add_book():
    title = request.form['title']
    author = request.form['author']
    possessor = request.form['possessor']

    book = models.Book(title, author, possessor)
    db.session.add(book)
    db.session.commit()

    return redirect(url_for('get_books'))

# to add users, unauthenticated
#
