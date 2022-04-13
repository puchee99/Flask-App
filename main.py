import os
#https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service?hl=en&authuser=1
#https://cloud.google.com/run/docs/mapping-custom-domains
#https://domains.google.com/registrar/arnaupuchevila.net/dns?hl=es&_ga=2.242095300.75589327.1649808138-555488080.1649808138

#https://support.google.com/a/answer/48090?hl=es-419
#gcloud init
##!!!!!! agafar codi de git com a airflow
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))