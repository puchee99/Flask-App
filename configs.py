from datetime import timedelta
#https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications
#https://flask-pymongo.readthedocs.io/en/latest/
#https://testdriven.io/blog/django-vs-flask/
#https://insaid.medium.com/setting-up-apache-airflow-in-macos-2b5e86eeaf1

# Statement for enabling the development environment
DEBUG = True
#pip install pyyaml
#import yaml
#yaml.safe_load("Dockerfile")#, Loader=yaml.FullLoader)
# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.sqlite') #'sqlite:///tables/users.sqlite3'
print(SQLALCHEMY_DATABASE_URI)
DATABASE_CONNECT_OPTIONS = {}
"""
MONGODB_SETTINGS = {
    'db': 'your_database',
    'host': 'localhost',
    'port': 27017
}
"""

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

SQLALCHEMY_TRACK_MODIFICATIONS = False
PERMANENT_SESSION_LIFETIME = timedelta(days=5)
