"""Blogly application."""

from crypt import methods
from site import USER_BASE
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


connect_db(app)
# db.create_all()

@app.route('/')
def home_page():
    """Redirects to a list of usesrs"""
    return redirect('/users')


@app.route('/users')
def list_users():
    """Shows all users with link to view details for each user
        Also have a link to add a new user form."""
    
    # query the entire database and save to a variable, then loop over each entry and display
    all_users = User.query.all()
    
    return render_template('list-users.html', all_users=all_users)


@app.route('/users/new')
def show_add_user_form():

    """GET Shows a form to add a new user with a button that posts to this same route."""
    return render_template('new-user-form.html')


@app.route('/users/new', methods=['POST'])
def add_user():
    """Process the user form and redirect back to /users"""

    # get the form inputs
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    image_url = request.form.get('image_url')

    # create a new instance of the User class using the user input
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    # add the new instance to the "session" (like git) using .add()
    db.session.add(new_user)
    # commit the new instance to the database using .commit()
    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:user_id>')
def show_user_info(user_id):
    """Shows user details with "edit" and "delete" button"""

    # query the databases for a user based on their ID using .get()
    curr_user = User.query.get_or_404(user_id)
    
    return render_template('user-detail-page.html', curr_user=curr_user)


@app.route('/users/<int:user_id>/edit')
def show_edit_user_form(user_id):
    """Shows the edit page for the user with a cancel button that returns
       to the detail page for the user, and also a save button to update
       the user"""

    # query the databases for a user based on their ID using .get()
    curr_user = User.query.get(user_id)

    return render_template('user-edit-page.html', curr_user=curr_user)


@app.route('/users/<int:user_id>/edit', methods = ['POST'])
def edit_user(user_id):
    """Processes the user edit form, then return the user to the /users page"""

    # query the databases for a user based on their ID using .get()
    curr_user = User.query.get(user_id)

    # edit the values base on the newly submitted form values
    curr_user.first_name = request.form.get('first_name')
    curr_user.last_name = request.form.get('last_name')
    curr_user.image_url = request.form.get('image_url')
    
    # add the edited instance to the "session" (like git) using .add()
    db.session.add(curr_user)
    # commit the new instance to the database using .commit()
    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    """Deletes the user."""

    User.query.filter_by(id=user_id).delete()

    db.session.commit()

    return redirect('/users')

################ ROUTES FOR POSTS ################

@app.route('/users/<int:user_id>/posts/new')
def show_add_post_form(user_id):
    """Show form to add a post for that user."""

    curr_user = User.query.get(user_id)

    return render_template('new-post-form.html', curr_user=curr_user)

@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def handle_add_post_form(user_id):
    """Handle add form; add post and redirect to the user detail page."""

    title = request.form.get('title')
    content = request.form.get('content')
    created_at = request.form.get('created_at')

    new_post = Post(title=title, content=content, created_at=created_at, user_id=user_id)

    # add the new instance to the "session" (like git) using .add()
    db.session.add(new_post)
    # commit the new instance to the database using .commit()
    db.session.commit()

    return redirect(f'/user/{user_id}')


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    """Show a post.
    Show buttons to edit and delete the post."""

    curr_post = Post.query.get(post_id)

    return render_template('post-detail-page.html', curr_post=curr_post)


@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):
    """Show form to edit a post, and to cancel (back to user page)."""

    curr_post = Post.query.get(post_id)

    return render_template('post-edit-page.html', curr_post=curr_post)


@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def handle_edit_post(post_id):
    """Handle editing of a post. Redirect back to the post view."""

    # query the databases for a post based on the ID using .get()
    curr_post = Post.query.get(post_id)

    # edit the values base on the newly submitted form values
    curr_post.title = request.form.get('title')
    curr_post.content = request.form.get('content')
    
    

    # add the edited instance to the "session" (like git) using .add()
    db.session.add(curr_post)
    # commit the new instance to the database using .commit()
    db.session.commit()

    return redirect(f'/posts/{post_id}')


@app.route('/posts/<int:post_id>/delete')
def delete_post(post_id):
    """Delete the post."""

    Post.query.filter_by(id=post_id).delete()

    db.session.commit()    

    return redirect('/')