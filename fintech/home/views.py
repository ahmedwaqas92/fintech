import sys
import json
import re
import base64
from flask import Flask, redirect, url_for, Blueprint, render_template, request, session
sys.path.append('../../')

import bcrypt
# from credentials.globalVariables import *
# from credentials.tokenInitialization import *
import requests


fintech_home = Blueprint("fintech_home", __name__, static_url_path="/var/www/html/fintech/fintech/home/static/", static_folder="static", template_folder="/var/www/html/fintech/fintech/home/templates")

@fintech_home.route("/")
def landing():
    return redirect(url_for("fintech_home.home"))


@fintech_home.route("/home")
def home():
	return render_template("home.html")


@fintech_home.route("/tempabout")
def aboutus():
	return redirect(url_for('fintech_about.about'))