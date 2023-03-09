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


fintech_aboutus = Blueprint("fintech_aboutus", __name__, static_url_path="/var/www/html/fintech/fintech/aboutus/static/", static_folder="static", template_folder="/var/www/html/fintech/fintech/aboutus/templates")

@fintech_aboutus.route("/aboutus")
def aboutus():
	return render_template("aboutus.html")



@fintech_aboutus.route("/temphome")
def temphome():
	return redirect(url_for("fintech_home.landing"))

@fintech_aboutus.route("/tempcontactus")
def tempcontactus():
	return redirect(url_for("fintech_contactus.contactus"))

# @fintech_aboutus.route("/templogin")
# def templogin():
# 	return redirect(url_for("fintech_login.login"))