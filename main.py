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
@app.route('/login', methods=['POST'])
def my_login():
	global fullname
	fullname = request.form.get('uname')
	pasword = request.form.get('pass')
	conn=psycopg2.connect("dbname=checker user=postgres password=areeba host=localhost")
	cur=conn.cursor()
	cur.execute("SELECT NAME,PASSWORD from userinfo where NAME=%s AND PASSWORD=%s",(fullname,pasword))
	rows=cur.fetchall()
	print("count is",len(rows))
	if (len(rows)==1):
		session['username']=fullname	
		session['password']=pasword
		print(session['username'])	
		print(session['password'])
		
		return render_template("make.html",username = session['username'])
	else:
		return("404 page")
@app.route('/mcqredirect')
def mcq_world():
	return render_template("make2.html",username = fullname,mcqtmarks=mcqtmarks,mpaper=mpaper)

@app.route('/theoryredirect')
def theory_world():
	return render_template("make3.html",username = fullname,thtmarks=thtmarks,thpaper=thpaper)

@app.route('/makeobjective', methods=['POST'])
def make_objective():
	
	# session['mcou'] = isset($_SESSION['mcou'] ? $_SESSION['mcou'] : 0);
	# mcqsession=session['mcou']
	session['mcou'] = session.get('mcou',0) 
	mcqnextbtn = request.form.get('mcq_next')
	mcqfinishbtn = request.form.get('mcq_finish')
	mcqpreviewbtn = request.form.get('mcq_preview')
	global mcqfinish_btn
	# os.remove('mcq.txt')
	
	
	

	

	if mcqnextbtn=='nextclick':
		session['mcou']+=1
		global mcqpaper
		global uid
		global mcqtmarks
		global mpaper
		mpaper = request.form.get('mcq_paper')
		mcqpaper = request.form.get('mcq_paper')+'mcq'
		mcqtmarks = request.form.get('mcq_tmarks')
		mcqques = request.form.get('mcq_ques')
		mcqmarks = request.form.get('mcq_marks')
		optiona = request.form.get('opta')
		optionb = request.form.get('optb')
		optionc = request.form.get('optc')
		optiond = request.form.get('optd')
		optione = request.form.get('opte')
		mcqnext_btn="true"
		mcqfinish_btn="false"
	
		conn=psycopg2.connect("dbname=checker user=postgres password=areeba host=localhost")
		cur=conn.cursor()
		# cur.execute("INSERT INTO  question (q_id,paper_name, total_marks, q_name,marks_of_q) VALUES(%s,%s,%s,%s,%s)",(session['mcou'],mcqpaper,mcqtmarks,mcqques,mcqmarks))
		# conn.commit()
		cur.execute("SELECT userid from userinfo where name=%s",(fullname,))
		rows=cur.fetchall()
		uid=rows[0][0]
		print(uid)
		cur.execute("SELECT paper_id from paper where paper_name=%s AND userid=%s",(mcqpaper,uid))
		rows=cur.fetchall()
		lenrows=len(rows)
		print("rows in paper is : ",len(rows))
	
		if(lenrows==0):
			conn=psycopg2.connect("dbname=checker user=postgres password=areeba host=localhost")
			cur=conn.cursor()
			cur.execute("INSERT INTO  paper (paper_name,userid) VALUES(%s,%s)",(mcqpaper,uid))
			conn.commit()
		cur.execute("SELECT paper_id from paper where paper_name=%s AND userid=%s",(mcqpaper,uid))
		rows=cur.fetchall()
		pid=rows[0][0]
		cur.execute("INSERT INTO  question (paper_id,q_id,userid) VALUES(%s,%s,%s)",(pid,session['mcou'],uid))
		conn.commit()
		cur.execute("UPDATE question SET paper_name=%s,total_marks=%s,q_name=%s,marks_of_q=1 WHERE userid=%s AND paper_id=%s AND q_id=%s",(mcqpaper,mcqtmarks,mcqques,uid,pid,session['mcou']))
		conn.commit()
		# writefile=open('mcq.txt','w')
		# paper="Subject: "+mpaper+"\r\n"
		# writefile.write(paper)
		# writefile.close()

		s1="Q"+str(session['mcou'])+": "+mcqques+"\r\n"
		s2="A)  "+optiona+"   B)  "+optionb+"   C)  "+optionc+"   D)  "+optiond+"   E)  "+optione+"\r\n"
		appendfile=open('mcq.txt','a')
		appendfile.write(s1)
		appendfile.write(s2)
		appendfile.close()
		print("inserted succesfully in question")
		return redirect(url_for('mcq_world',_anchor='mcq_marks'))
    elif mcqfinishbtn=='finishclick':
		session['mcou']+=1
		mpaper = request.form.get('mcq_paper')
		mcqpaper = request.form.get('mcq_paper')+'mcq'
		mcqtmarks = request.form.get('mcq_tmarks')
		mcqques = request.form.get('mcq_ques')
		mcqmarks = request.form.get('mcq_marks')
		optiona = request.form.get('opta')
		optionb = request.form.get('optb')
		optionc = request.form.get('optc')
		optiond = request.form.get('optd')
		optione = request.form.get('opte')
		
		mcqfinish_btn="true"
		conn=psycopg2.connect("dbname=checker user=postgres password=areeba host=localhost")
		cur=conn.cursor()
		cur.execute("SELECT userid from userinfo where name=%s",(fullname,))
		rows=cur.fetchall()
		uid=rows[0][0]
		# print(user_id)
		# cur.execute("INSERT INTO  paper (paper_name,userid) VALUES(%s,%s)",(mcqpaper,uid))
		# conn.commit()
		cur.execute("SELECT paper_id from paper where paper_name=%s AND userid=%s",(mcqpaper,uid))
		rows=cur.fetchall()
		pid=rows[0][0]
		cur.execute("INSERT INTO  question (paper_id,q_id,userid) VALUES(%s,%s,%s)",(pid,session['mcou'],uid))
		conn.commit()
		cur.execute("UPDATE question SET paper_name=%s,total_marks=%s,q_name=%s,marks_of_q=1 WHERE userid=%s AND paper_id=%s AND q_id=%s",(mcqpaper,mcqtmarks,mcqques,uid,pid,session['mcou']))
		conn.commit()

		s1="Q"+str(session['mcou'])+": "+mcqques+"\r\n"
		s2="A)  "+optiona+"   B)  "+optionb+"   C)  "+optionc+"   D)  "+optiond+"   E)  "+optione+"\r\n"
		appendfile=open('mcq.txt','a')
		appendfile.write(s1)
		appendfile.write(s2)
		appendfile.close()
		print("inserted succesfully in question")
		session.pop('mcou',None)
		session['mcou'] = session.get('mcou',0) 

		# cur.execute("INSERT INTO  question (q_id,paper_name, total_marks, q_name,marks_of_q) VALUES(%s,%s,%s,%s,%s)",(session['mcou'],mcqpaper,mcqtmarks,mcqques,mcqmarks))
		# conn.commit()
		# cur.execute("SELECT paper_id,paper_name from paper where paper_name=%s AND userid=%s",(mcqpaper,uid))
		# rows=cur.fetchall()
		# pid=rows[0][0]
		# print("paper_id: ",pid)
		# pname=rows[0][1]
		# print("paer_name: ",pname)
		# cur.execute("UPDATE question SET paper_id=%s WHERE paper_name=%s AND userid=%s",(pid,pname,uid))
		# conn.commit()
		return redirect(url_for('mcq_world',_anchor='mcq_marks'))
    elif  mcqpreviewbtn=='previewclick':
		mpaper = request.form.get('mcq_paper')
		mcqpaper = request.form.get('mcq_paper')+'mcq'
		mcqtmarks = request.form.get('mcq_tmarks')
		mcqques = request.form.get('mcq_ques')
		mcqmarks = request.form.get('mcq_marks')
		writefile=open('mcq.txt','a')
		paper="Subject: "+mpaper+"\r\n"
		totalmarks="Total Marks: "+mcqtmarks+"\r\n"
		session.pop('mcou',None)

		writefile.write(paper)
		writefile.write(totalmarks)
		writefile.close()
		# if mcqfinish_btn=="false":
		# 	print("mcqfinishbtn is ",mcqfinish_btn)
		# 	conn=psycopg2.connect("dbname=checker user=postgres password=areeba host=localhost")
		# 	cur=conn.cursor()
		# 	cur.execute("SELECT userid from userinfo where name=%s",(fullname,))
		# 	rows=cur.fetchall()
		# 	uid=rows[0][0]
		# 	# cur.execute("INSERT INTO  paper (paper_name,userid) VALUES(%s,%s)",(mcqpaper,uid))
		# 	# conn.commit()
		# 	cur.execute("SELECT paper_id,paper_name from paper where paper_name=%s AND userid=%s",(mcqpaper,uid))
		# 	rows=cur.fetchall()
		# 	pid=rows[0][0]
		# 	print("paper_id: ",pid)
		# 	pname=rows[0][1]
		# 	print("paer_name: ",pname)
		# 	session['mcou'] = session.get('mcou',0) 
		# 	# cur.execute("UPDATE question SET paper_id=%s WHERE paper_name=%s AND userid=%s",(pid,pname,uid))
		# 	# conn.commit()
		# 	# cur.execute("INSERT INTO  question (paper_id,q_id,userid) VALUES(%s,%s,%s)",(pid,session['mcou'],uid))
		# 	# conn.commit()
		# 	# cur.execute("UPDATE question SET paper_name=%s,total_marks=%s,q_name=%s,marks_of_q=1 WHERE userid=%s AND paper_id=%s AND q_id=%s",(mcqpaper,mcqtmarks,mcqques,uid,pid,session['mcou']))
		# 	# conn.commit()
		# 	# print("finish is",mcqfinish_btn)
		# 	session['mcou'] = session.get('mcou',0) 


		# session['mcou'] = session.get('mcou',0) 
		return redirect(url_for('mcqpdf'))
		# return render_template("make.html",username = session['username'])
        @app.route('/mcqpdf')
def mcqpdf():
	pdf=FPDF()
	pdf.add_page()
	pdf.set_font('Arial','B',14)
	pdf.cell(100, 7, """          								                XYZ School Of Education And Excellence""",0,1 )
	pdf.cell(100, 7, """          								 
																   EXAMINATIONS:2017-2018""",0,1 )
	pdf.cell(100, 7, """           								 
																          BATCH:2014-2015""",0,1 )
	filepath = 'mcq.txt'  
	with open('mcq.txt') as f:
		for i, l in enumerate(f):
			pass
		rows= i  
	with open(filepath) as fp:
		line = fp.readline()
		cnt = 1
		while line:
			if cnt==rows-2:
				pdf.set_font('Arial','B',14)
				pdf.cell(100, 7, "																          		   				            "+line.strip() + "                         \r\n",0,1 )
			line = fp.readline()
			cnt += 1
	with open('mcq.txt') as f:
		for i, l in enumerate(f):
			pass
		rows= i  
	with open(filepath) as fp:
		line = fp.readline()
		cnt = 1
		while line:
			if cnt==rows:
				pdf.set_font('Arial','B',14)
				pdf.cell(101, 7, "																          		   				                                                              "+line.strip() + "                         \r\n",0,1 )
			line = fp.readline()
			cnt += 1
	pdf.cell(100, 7, "",0,1 )
	pdf.cell(100, 7, "Time:30mins\n",0,1 )
	pdf.cell(100, 7, "",0,1 )
	pdf.set_font('Arial','', 14)
	pdf.cell(100, 7, "Instruction:",0,1 )
	pdf.cell(100, 7, "			Read Paper Carefully",0,1 )
	pdf.cell(100, 7, "",0,1 )
	pdf.cell(100, 7, "",0,1 )
	pdf.set_font('Arial','', 14)
	filepath = 'mcq.txt'
	with open('mcq.txt') as f:
		for i, l in enumerate(f):
			pass
		rows= i 
		secondlastrow=i-2 
	with open(filepath) as fp:
		line = fp.readline()
		cnt = 1
		while line:
			# if cnt!=rows:
			# 	pdf.cell(120, 7, "\r\n"+line.strip() + "                         \r\n",0,1 )

			# if cnt!=rows and cnt%2!=0:
			# 	pdf.cell(120, 7, "\r\n"+"Q"+str(cnt)+": "+line.strip() + "                         \r\n",0,1 )
			# 	cnt += 1
			# elif cnt!=rows and cnt%2==0:
			# 	pdf.cell(120, 7, "\r\n"+line.strip() + "                         \r\n",0,1 )
			# 	cnt += 1
			# line = fp.readline()

			# cnt += 1
			if cnt!=rows:
				if cnt!=secondlastrow:
					pdf.cell(120, 7, "\r\n"+line.strip() + "                         \r\n",0,1 )
				
			line = fp.readline()

			cnt += 1
    if (os.path.isfile('templates/pdfdemo.pdf')):
		os.remove('templates/pdfdemo.pdf')
	if (os.path.isfile('mcq.txt')):
		os.remove('mcq.txt')
	
	# print("rows is :"+str(rows))
	# with open("mcq.txt", "r") as lst:
	# 	for i in range(0,rows):
	# 		item=""
	# 		# item[0]=lst[.read().splitlines()]
	# 		item=lst[0]
	# 		print("Item is "+item)
	# 		pdf.cell(120, 7, "\r\n"+str(lst.read().splitlines()) + "                         \r\n",0,1 )

		# print(lst.read().splitlines())
	# file = open("mcq.txt",'r')
	# for i in range(max(0, rows-100),rows,1):
	# 	pdf.cell(120, 7, "\r\n"+file[i] + "                         \r\n",0,1 )

    # for i = max(0, count(file)-100); i < count(file); i+=1:
    # 	pdf.cell(120, 7, "\r\n".file[i] . "                         \r\n",0,1 )

	pdf.output('templates/pdfdemo.pdf','F')
	return send_from_directory(directory='templates',
                               filename='pdfdemo.pdf',
                               mimetype='application/pdf')
	# return render_template("pdfdemo.pdf")
@app.route('/makedescriptive', methods=['POST'])
def make_descriptive():
	
	# session['mcou'] = isset($_SESSION['mcou'] ? $_SESSION['mcou'] : 0);
	# mcqsession=session['mcou']
	session['tcou'] = session.get('tcou',0) 
	thnextbtn = request.form.get('th_next')
	thfinishbtn = request.form.get('th_finish')
	thpreviewbtn = request.form.get('th_preview')
	global thfinish_btn
	# os.remove('mcq.txt')
	
	
	

	

	if thnextbtn=='thnextclick':
        session['tcou']+=1
		global thpaper
		global uid
		global thtmarks
		global thpaper
		thpaper = request.form.get('th_paper')
		thtmarks = request.form.get('th_tmarks')
		thques = request.form.get('th_ques')
		thmarks = request.form.get('th_marks')
	
		thnext_btn="true"
		thfinish_btn="false"
       conn=psycopg2.connect("dbname=checker user=postgres password=areeba host=localhost")
		cur=conn.cursor()
		# cur.execute("INSERT INTO  question (q_id,paper_name, total_marks, q_name,marks_of_q) VALUES(%s,%s,%s,%s,%s)",(session['mcou'],mcqpaper,mcqtmarks,mcqques,mcqmarks))
		# conn.commit()
		cur.execute("SELECT userid from userinfo where name=%s",(fullname,))
		rows=cur.fetchall()
		uid=rows[0][0]
		print(uid)
		cur.execute("SELECT paper_id from paper where paper_name=%s AND userid=%s",(thpaper,uid))
		rows=cur.fetchall()
		lenrows=len(rows)
		print("rows in paper is : ",len(rows))
	
		if(lenrows==0):
            conn=psycopg2.connect("dbname=checker user=postgres password=areeba host=localhost")
			cur=conn.cursor()
			cur.execute("INSERT INTO  paper (paper_name,userid) VALUES(%s,%s)",(thpaper,uid))
			conn.commit()
		cur.execute("SELECT paper_id from paper where paper_name=%s AND userid=%s",(thpaper,uid))
		rows=cur.fetchall()
		pid=rows[0][0]
       cur.execute("INSERT INTO  question (paper_id,q_id,userid) VALUES(%s,%s,%s)",(pid,session['tcou'],uid))
		conn.commit()
		cur.execute("UPDATE question SET paper_name=%s,total_marks=%s,q_name=%s,marks_of_q=%s WHERE userid=%s AND paper_id=%s AND q_id=%s",(thpaper,thtmarks,thques,thmarks,uid,pid,session['tcou']))
		conn.commit()
		# writefile=open('mcq.txt','w')
		# paper="Subject: "+mpaper+"\r\n"
		# writefile.write(paper)
		# writefile.close()

		s1="Q"+str(session['tcou'])+": "+thques+"   "+"("+thmarks+"Marks)\r\n"
		appendfile=open('theory.txt','a')
		appendfile.write(s1)
		appendfile.close()
		print("inserted succesfully in question")
		return redirect(url_for('theory_world',_anchor='th_tmarks'))

	elif thfinishbtn=='thfinishclick':
		session['tcou']+=1
       thpaper = request.form.get('th_paper')
		thtmarks = request.form.get('th_tmarks')
		thques = request.form.get('th_ques')
		thmarks = request.form.get('th_marks')
		
		thfinish_btn="true"
		conn=psycopg2.connect("dbname=checker user=postgres password=areeba host=localhost")
		cur=conn.cursor()
		cur.execute("SELECT userid from userinfo where name=%s",(fullname,))
		rows=cur.fetchall()
		uid=rows[0][0]
		# print(user_id)
		# cur.execute("INSERT INTO  paper (paper_name,userid) VALUES(%s,%s)",(mcqpaper,uid))
		# conn.commit()
		cur.execute("SELECT paper_id from paper where paper_name=%s AND userid=%s",(thpaper,uid))
		rows=cur.fetchall()
		pid=rows[0][0]
		cur.execute("INSERT INTO  question (paper_id,q_id,userid) VALUES(%s,%s,%s)",(pid,session['tcou'],uid))
		conn.commit()
		cur.execute("UPDATE question SET paper_name=%s,total_marks=%s,q_name=%s,marks_of_q=%s WHERE userid=%s AND paper_id=%s AND q_id=%s",(thpaper,thtmarks,thques,thmarks,uid,pid,session['tcou']))
		conn.commit()

		s1="Q"+str(session['tcou'])+": "+thques+"   "+"("+thmarks+"Marks)\r\n"
		appendfile=open('theory.txt','a')
		appendfile.write(s1)
		appendfile.close()
		print("inserted succesfully in question")
		session.pop('tcou',None)
		session['tcou'] = session.get('tcou',0) 

		return redirect(url_for('theory_world',_anchor='th_marks'))

	elif  thpreviewbtn=='thpreviewclick':
		thpaper = request.form.get('th_paper')
		thtmarks = request.form.get('th_tmarks')
		thques = request.form.get('th_ques')
		thmarks = request.form.get('th_marks')
		writefile=open('theory.txt','a')
		paper="Subject: "+thpaper+"\r\n"
		totalmarks="Total Marks: "+thtmarks+"\r\n"
		session.pop('tcou',None)

		writefile.write(paper)
		writefile.write(totalmarks)
		writefile.close()
		 
		return redirect(url_for('theorypdf'))
			
 
    
            

