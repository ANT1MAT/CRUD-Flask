from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Wishlist(db.Model):
    __tablename__ = 'list'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(100))
    disc = db.Column(db.String(100))
