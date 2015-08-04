from app import db

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    author = db.Column(db.String())
    possessor = db.Column(db.String())

    def __init__(self, title, author, possessor):
        self.title = title
        self.author = author
        self.possessor = possessor

    def __repr__(self):
        return '<id {}>'.format(self.id)

# adding user model
class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String())
    l_name = db.Column(db.String())
    favorite_color = db.Column(db.String())

    def __init__(self, f_name, l_name, favorite_color):
        self.f_name = f_name
        self.l_name = l_name
        self.favorite_color = favorite_color

    def __repr__(self):
        return '<first name {}>'.format(self.f_name)

