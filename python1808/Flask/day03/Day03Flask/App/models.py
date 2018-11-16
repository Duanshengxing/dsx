from .exts import db

collects = db.Table(
    'collects',
    db.Column('book_id',db.Integer,db.ForeignKey('book.id'),primary_key=True),
    db.Column('publisher_id',db.Integer,db.ForeignKey('publisher.id'),primary_key=True),
)




class Author(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),unique=True)
    age = db.Column(db.Integer,default=0)
    sex = db.Column(db.Boolean,default=1)
    email = db.Column(db.String(80),default='')
    books = db.relationship('Book', backref='bktoat', lazy=True)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    date = db.Column(db.Date)
    author = db.Column(db.Integer, db.ForeignKey(Author.id))
    publishers = db.relationship('Publisher', backref='pbtobook', secondary=collects, lazy=True)


class Publisher(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(60),unique=True)
    address = db.Column(db.String(200))
    city = db.Column(db.String(50))
    province = db.Column(db.String(50))
    country = db.Column(db.String(50))
    website = db.Column(db.String(100))


