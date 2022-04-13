#COPIAT TOT, REVISAR
# 
# 
# 
# # Import flask and template operators




#RUN and search--> http://[your droplet's IP]/auth/signin
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

#from flask_mongoengine import MongoEngine

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('configs')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

#db_mongo = MongoEngine(app)
#db_mongo.init_app(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth.views import mod_auth as auth_module
#from app.mod_auth_2.views import mod_auth_2 as auth_module_2

# Register blueprint(s)
app.register_blueprint(auth_module)
#app.register_blueprint(auth_module_2)

# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

#from library.scraper import data_scrapper
#data_scrapper()
from app.mod_auth.dash_plots import create_dash
create_dash(app)
