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

    # define our relationship for posts to users, and backref
    # the first arg in the relationship method is the class name
    # of the model we want to reference with this relationship
    user = db.relationship('User', backref='posts')

    # define our relationship for posts to tags, and backref
    # we backref to "post" because  we are making this relationship
    # from the post to the post_tags table and back
    # posts_tags = db.relationship('PostTag', backref='post')

    # using through relationship
    tags = db.relationship('Tag', secondary='posts_tags', backref='posts')

    def __repr__(self):
        """Show Info about post"""
        p = self
        return f"<Post id={p.id} title={p.title} created_at={p.created_at} user_id={p.user_id}>"


class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.String(20),
                    unique=True,
                    nullable=False)

    # define our relationship for posts to tags, and backref
    # we backref to "post" because  we are making this relationship
    # from the post to the post_tags table and back
    # posts_tags = db.relationship('PostTag', backref='tag')

    def __repr__(self):
        """Show Info about post"""
        t = self
        return f"<Tag id={t.id} name={t.name}>"


class PostTag(db.Model):
    __tablename__ = "posts_tags"

    post_id = db.Column(db.Integer,
                        db.ForeignKey('posts.id'),
                        primary_key=True,
                        nullable=False)
    tag_id = db.Column(db.Integer,
                        db.ForeignKey('tags.id'),
                        primary_key=True,
                        nullable=False)

    def __repr__(self):
        """Show Info about post"""
        pt = self
        return f"<PostTag post_id={pt.post_id} tag_id={pt.tag_id}>"