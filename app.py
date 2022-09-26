"""Blogly application."""

from crypt import methods
from site import USER_BASE
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

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