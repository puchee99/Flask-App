
#https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service?hl=en&authuser=1
#https://cloud.google.com/run/docs/mapping-custom-domains
#https://domains.google.com/registrar/arnaupuchevila.net/dns?hl=es&_ga=2.242095300.75589327.1649808138-555488080.1649808138

#https://support.google.com/a/answer/48090?hl=es-419
#gcloud init
##!!!!!! agafar codi de git com a airflow


if __name__ == "__main__":

    # We need to make sure Flask knows about its views before we run
    # the app, so we import them. We could do it earlier, but there's
    # a risk that we may run into circular dependencies, so we do it at the
    # last minute here.

    #from views.basic import *
    from app import app ##

    app.run(host='0.0.0.0', port=105,use_reloader=True,debug=True)#http://localhost:105/hello/


"""
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello mitrwq fav24 {}!".format(name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

"""