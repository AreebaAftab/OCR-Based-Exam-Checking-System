# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 18:05:23 2018

@author: Areeba aftab
"""

from flask import Flask,render_template,request,session,redirect,url_for,send_from_directory,send_file
import sys
from flask_uploads import UploadSet,configure_uploads,TEXT
import _decimal

# import cdecimal
# from cdecimal import Decimal
from _decimal import Decimal

#import warnings
#warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.corpus import wordnet as wn
from os import path

import psycopg2
import fpdf
from fpdf import FPDF
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import os.path

import pymysql
# with __main__.test_request_context():
# 	session['mcou']


app=Flask(__name__)
app.secret_key = os.urandom(24)
@app.route('/')
def index():
	return render_template("index.html")
@app.route('/logout')
def logout():
	return render_template("index.html")
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route('/signin')
def signin():
	return render_template("signin.html")
@app.route('/signup')
def signup():
	return render_template("signup.html")
def check():
	return render_template("check.html",username = fullname)
@app.route('/result')
def result():
	return render_template("result.html",username = fullname)
@app.route('/account', methods=['POST'])
def my_account():
	fullname = request.form.get('fullname')
	email = request.form.get('email')
	password = request.form.get('pass')
	paymentmethod = request.form.get('payment-method')
	cardno = request.form.get('cardno')
	cvc = request.form.get('cvc')
	conn=psycopg2.connect("dbname=checker user=postgres password=areeba host=localhost")
	cur=conn.cursor()
	cur.execute("INSERT INTO  userinfo (name,email,password,payment_type,cardno,cvc) VALUES(%s,%s,%s,%s,%s,%s)",(fullname,email,password,paymentmethod,cardno,cvc))
	conn.commit()
	return render_template("signin.html")