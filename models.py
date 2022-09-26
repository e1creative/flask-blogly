"""Models for Blogly."""
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer,
                primary_key=True,
                autoincrement=True)
    first_name = db.Column(db.String(20),
                        nullable=False)
    last_name = db.Column(db.String(20),
                        nullable=False)
    image_url = db.Column(db.Text)

    def __repr__(self):
        """Show Info about pet"""
        u = self
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name} image_url={u.image_url}>"

    def get_full_name(self):
        """Return user first name + last name."""
        return f"{self.first_name} {self.last_name}"


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer,
                primary_key=True,
                autoincrement=True)
    title = db.Column(db.String(20),
                        nullable=False)
    content = db.Column(db.String(100),
                        nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow,
                        nullable=False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'))

    user = db.relationship('User', backref='posts')

    def __repr__(self):
        """Show Info about post"""
        p = self
        return f"<Post id={p.id} title={p.title} created_at={p.created_at} user_id={p.user_id}>"