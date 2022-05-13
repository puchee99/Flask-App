from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

from app import db

# Import module models (i.e. User)
from app.mod_auth.models import Users, create_user#, Users_mongo


mod_auth = Blueprint('auth', __name__, url_prefix='')

from werkzeug.security import generate_password_hash, check_password_hash

from app.mod_auth.forms import LoginForm
import json
from flask import Flask, request, jsonify

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
    
