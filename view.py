# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 00:29:43 2018

@author: Areeba aftab
"""

from flask import Flask
from flask import redirect, url_for,render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
	return render_template("try.html")
    


@app.route('/myredirect')
def my_redirect():
    return redirect(url_for('hello_world',_anchor='my_anchor'))


if __name__ == '__main__':
    app.run()