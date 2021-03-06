# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 20:23:39 2019

@author: georgin
"""

from flask import Flask, render_template, request
import logging
import mail_api_example2

flask_app = Flask(__name__)

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

@flask_app.route('/')
def show():
    return render_template('index.html')

@flask_app.route('/after')
def show2():
    return render_template('index2.html')

@flask_app.route('/form')
def form():
    return render_template('form.html')

@flask_app.route('/submit',methods=['POST'])
def email():
    if request.method == 'POST':
        country = request.form['countries']
        contact = request.form['s']
        message = request.form['m']
        mail_api_example2.sendmail(country,contact,message)
    return render_template('submit.html',value=contact)

logger.info('STARTING APP, TRY IT OUT!!!')

flask_app.run(debug=True, use_reloader=True)