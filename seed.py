from models import db, User, Post, Tag, PostTag
from app import app

db.drop_all()
db.create_all()

User.query.delete()
Post.query.delete()
Tag.query.delete()
PostTag.query.delete()


##### USER #####

u1 = User(first_name='John', last_name='Smith', image_url='https://source.unsplash.com/random/300×300')
u2 = User(first_name='James', last_name='Wick', image_url='https://source.unsplash.com/random/300×300')
u3 = User(first_name='Jason', last_name='Takahashi', image_url='https://source.unsplash.com/random/300×300')
u4 = User(first_name='Shu', last_name='Nishide', image_url='https://source.unsplash.com/random/300×300')

db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)

db.session.commit()


##### POST #####

p1 = Post(title='Hello World', content='My very first blog post!', created_at='2022/01/01', user_id='1')
p2 = Post(title='Flask Is Awesome', content='Flask is a lvoely framework for building cool things.', created_at='2022/01/01', user_id='2')
p3 = Post(title='Yet Another Post', content='Here is the content', created_at='2022/01/01', user_id='3')
p4 = Post(title='My Birthday', content='Today is my birthday! I\'m taking the day off!', created_at='2022/01/01', user_id='4')
p5 = Post(title='New Car', content='Bought a new car today!  I got a Tesla!', created_at='2022/01/01', user_id='1')
p6 = Post(title='New Job', content='Just started my new job!  So far, so good!', created_at='2022/01/01', user_id='2')
p7 = Post(title='Tonights Dinner', content='Tonights dinner...ramen!', created_at='2022/01/01', user_id='3')
p8 = Post(title='Breafast at Tiffanys', content='Literally, had breakfast at Tiffanys!', created_at='2022/01/01', user_id='4')

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.add(p5)
db.session.add(p6)
db.session.add(p7)
db.session.add(p8)

db.session.commit()


##### TAG #####

t1 = Tag(name='food')
t2 = Tag(name='event')
t3 = Tag(name='random')
t4 = Tag(name='daily')

db.session.add(t1)
db.session.add(t2)
db.session.add(t3)
db.session.add(t4)

db.session.commit()

##### POSTTAG #####

pt1 = PostTag(post_id='1', tag_id='1')
pt2 = PostTag(post_id='2', tag_id='1')
pt3 = PostTag(post_id='3', tag_id='4')
pt4 = PostTag(post_id='1', tag_id='2')

db.session.add(pt1)
db.session.add(pt2)
db.session.add(pt3)
db.session.add(pt4)

db.session.commit()