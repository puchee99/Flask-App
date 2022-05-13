
from app import db#, db_mongo

class Users(db.Model):
    # See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self,name,email):
        self.name = name
        self.email = email


def create_user(new_name, new_email):
    # Create a dessert with the provided input.
    # At first, we will trust the user.

    # This line maps to line 16 above (the Dessert.__init__ method)
    usr = Users(new_name, new_email)

    # Actually add this dessert to the database
    db.session.add(usr)

    # Save all pending changes to the database
    db.session.commit()

    return usr
