
if __name__ == "__main__":

    # We need to make sure Flask knows about its views before we run
    # the app, so we import them. We could do it earlier, but there's
    # a risk that we may run into circular dependencies, so we do it at the
    # last minute here.

    #from views.basic import *
    from app import app ##

    app.run(host='0.0.0.0', port=105,use_reloader=True,debug=True)
