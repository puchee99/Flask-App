#from sqlite3 import dbapi2
#import sys
#sys.path.append("..")
#from run import db
from app import db#, db_mongo

#from library.scraper import data_scrapper

class Users(db.Model):
    # See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self,name,email):
        self.name = name
        self.email = email
"""
class Users_mongo(db_mongo.Document):
    name = db_mongo.StringField()
    email = db_mongo.StringField()
    def to_json(self):
        return {"name": self.name,
                "email": self.email}
"""


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



#if __name__ == "__main__":

    # Run this file directly to create the database tables.
    #data_scrapper()
    #db.create_all()
    #python models.py to create db
"""


def create_pdf(df, name ="Stock"):
    day = str(datetime.now()).split()[0]
    canvas = Canvas("pdf/"+name+day+".pdf")
    canvas.drawString(72, 72, "Hello, World")

    canvas.save()
    return
    if "-t" in opts: #train
        data = ql.call2()
        print(data.head())
        print(data.tail())

    ml.run()
"""