from models import db, User
from app import app

db.drop_all()
db.create_all()

User.query.delete()

u1 = User(first_name='John', last_name='Smith', image_url='https://source.unsplash.com/random/300×300')
u2 = User(first_name='James', last_name='Wick', image_url='https://source.unsplash.com/random/300×300')
u3 = User(first_name='Jason', last_name='Takahashi', image_url='https://source.unsplash.com/random/300×300')
u4 = User(first_name='Shu', last_name='Nishide', image_url='https://source.unsplash.com/random/300×300')

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)

# need to commit the files to the sql database
db.session.commit()