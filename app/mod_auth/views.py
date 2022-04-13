from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
#import sys
#sys.path.append("..")

# Import the database object from the main app module
from app import db

# Import module models (i.e. User)
from app.mod_auth.models import Users, create_user#, Users_mongo
#from run import app




################mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

mod_auth = Blueprint('auth', __name__, url_prefix='')

from werkzeug.security import generate_password_hash, check_password_hash

from app.mod_auth.forms import LoginForm
import json
from flask import Flask, request, jsonify
"""
#START MONGO
@mod_auth.route('/movies')
def  get_movies():
    movies = Users_mongo.objects()
    return  jsonify(movies), 200


@mod_auth.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    user = Users_mongo.objects(name=name).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())

@mod_auth.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    user = Users_mongo(name=record['name'],
                email=record['email'])
    user.save()
    return jsonify(user.to_json())

@mod_auth.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    user = Users_mongo.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.update(email=record['email'])
    return jsonify(user.to_json())

@mod_auth.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    user = Users_mongo.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.delete()
    return jsonify(user.to_json())

#END MONGO
"""

###########@mod_auth.route('/login', methods=['GET', 'POST'])

@mod_auth.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        session.permanent = True
        dessert_cals = request.form.get('cals_field')
        user= request.form["nm"]#post--secure formatted data
        session["user"] = user #semblant cookies

        found_users = Users.query.filter_by(name=user).first()
        if found_users:
            session["email"] = found_users.email

        else:
            
            create_user(user, "")

        flash("login succes")
        return redirect(url_for("auth.user"))
    else:
        if "user" in session:
            flash("Already login")
            return redirect(url_for("auth.user"))
        return render_template("auth/login.html")

@mod_auth.route("/user", methods=['GET', 'POST'])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"] # or dessert_name = request.form.get('name_field')
            found_users = Users.query.filter_by(name=user).first()
            #record = json.loads(request.data)
            user_mongo = Users_mongo(name=user,
                email=email)
            user_mongo.save()
            print('saved')
            create_user(user, email)
            session["email"] =email
            flash("Email was saved")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("auth/user.html", email=email)
    else:
        flash("You are not login")
        return redirect(url_for("auth.login"))

@mod_auth.route("/logout")
def logout():
    flash("You are logout, ", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("auth.login"))

@mod_auth.route("/view")
def view():
    return render_template("auth/view.html", values=Users.query.all())
@mod_auth.route("/home")
def home():
    return render_template("auth/index.html")



# Set the route and accepted methods
@mod_auth.route('/signin/', methods=['GET', 'POST'])
def signin():

    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = Users.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):

            session['user_id'] = user.id

            flash('Welcome %s' % user.name)

            return redirect(url_for('auth.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("auth/signin.html", form=form)
    






"""
@app.route('/')
def index():

    desserts = Dessert.query.all()

    return render_template('index.html', desserts=desserts)


@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'GET':
        return render_template('add.html')

    # Because we 'returned' for a 'GET', if we get to this next bit, we must
    # have received a POST

    # Get the incoming data from the request.form dictionary.
    # The values on the right, inside get(), correspond to the 'name'
    # values in the HTML form that was submitted.

    dessert_name = request.form.get('name_field')
    dessert_price = request.form.get('price_field')
    dessert_cals = request.form.get('cals_field')

    dessert = create_dessert(dessert_name, dessert_price, dessert_cals)
    return render_template('add.html', dessert=dessert)
"""