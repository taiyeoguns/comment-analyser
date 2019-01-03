from datetime import datetime
from app import db

class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(25), unique=True)
    text = db.Column(db.String(50))
    owner = db.Column(db.String(25))
    tone = db.Column(db.String(25))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """
        String representation of object
        """
        return f'Comment: "{self.sku} - {self.text}" - written by: {self.owner}'
