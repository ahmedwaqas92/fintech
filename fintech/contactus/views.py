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


fintech_contactus = Blueprint("fintech_contactus", __name__, static_url_path="/var/www/html/fintech/fintech/contactus/static/", static_folder="static", template_folder="/var/www/html/fintech/fintech/contactus/templates")

@fintech_contactus.route("/contactus")
def contactus():
	return render_template("contactus.html")



@fintech_contactus.route("/temphome")
def temphome():
	return redirect(url_for("fintech_home.landing"))

@fintech_contactus.route("/tempaboutus")
def tempaboutus():
	return redirect(url_for("fintech_aboutus.aboutus"))

# @fintech_aboutus.route("/templogin")
# def templogin():
# 	return redirect(url_for("fintech_login.login"))