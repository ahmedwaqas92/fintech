import os

from flask import Flask, render_template
from fintech.home.views import fintech_home
from fintech.aboutus.views import fintech_aboutus
from fintech.contactus.views import fintech_contactus

# from credentials.globalVariables import *
# from credentials.tokenInitialization import *

app = Flask(__name__)
# app.secret_key = ASTRA_DB_APPLICATION_TOKEN
app.secret_key = "TemperoryASTRAKEY123456789"
app.session_cookie_path = '/'


app.register_blueprint(fintech_home, url_prefix="/fintech")
app.register_blueprint(fintech_aboutus, url_prefix="/fintech")
app.register_blueprint(fintech_contactus, url_prefix="/fintech")
# app.register_blueprint(fintech_login, url_prefix="/fintech")


@app.route("/")
def test():
    return "<h1>Fintech Prefix</h1>"

if __name__ == '__main__':
    app.run(debug=True)
