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
