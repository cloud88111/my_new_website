# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 20:23:39 2019

@author: georgin
"""

from flask import Flask, render_template
import logging

flask_app = Flask(__name__)

#CONFIGURING LOGGING
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

fh = logging.FileHandler('application_logs.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

"""def hello_someone(name):
    return render_template("hello.html", name=name.title())"""

@flask_app.route('/')
@flask_app.route("/index")
def show():
    return render_template('index2.html')

logger.info('STARTING APP, TRY IT OUT!!!')
  
flask_app.run(debug=True, use_reloader=True)