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
			
@app.route('/theorypdf')
def theorypdf():
	pdf=FPDF()
	pdf.add_page()
	pdf.set_font('Arial','B',14)
	pdf.cell(100, 7, """          								                XYZ School Of Education And Excellence""",0,1 )
	pdf.cell(100, 7, """          								 
																   EXAMINATIONS:2017-2018""",0,1 )
	pdf.cell(100, 7, """           								 
																          BATCH:2014-2015""",0,1 )
	filepath = 'theory.txt'  
	with open('theory.txt') as f:
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
	with open('theory.txt') as f:
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
	pdf.cell(100, 7, "Time:150mins\n",0,1 )
	pdf.cell(100, 7, "",0,1 )
	pdf.set_font('Arial','', 14)
	pdf.cell(100, 7, "Instruction:",0,1 )
	pdf.cell(100, 7, "			Read Paper Carefully",0,1 )
	pdf.cell(100, 7, "",0,1 )
	pdf.cell(100, 7, "",0,1 )
	pdf.set_font('Arial','', 14)
	filepath = 'theory.txt'
	with open('theory.txt') as f:
		for i, l in enumerate(f):
			pass
		rows= i 
		secondlastrow=i-2 
	with open(filepath) as fp:
		line = fp.readline()
		cnt = 1
		while line:
			
			if cnt!=rows:
				if cnt!=secondlastrow:
					pdf.cell(120, 7, "\r\n"+line.strip() + "                         \r\n",0,1 )
				
			line = fp.readline()

			cnt += 1
    
	if (os.path.isfile('theory.txt')):
		os.remove('theory.txt')
	
	
	pdf.output('templates/theorypdf.pdf','F')
	return send_from_directory(directory='templates',
                               filename='theorypdf.pdf',
                               mimetype='application/pdf')
	if (os.path.isfile('templates/theorypdf.pdf')):
		os.remove('templates/theorypdf.pdf')
	# return render_template("pdfdemo.pdf")
@app.route("/uploadstudent", methods=["POST"])
def uploadstudent():
	global mcqpaper
	global mpaper
	global mstdfilename
	global stdmcqdestination
   
	mcqpaper = request.form.get('mcq_paper')
	mpaper = request.form.get('mcq_paper')+'mcq'
    #target = os.path.join(APP_ROOT,'/studentmcq')
 
	target ="C:/Users/Areeba Aftab/Desktop/checker/flask"

	print(target)
	if not os.path.isdir(target):
		os.mkdir(target)
   #for file in request.files.getlist("mcqstd_file"):

	for file in request.files.getlist("mcqstd_file"):
		print(file)

		mstdfilename = "002.png"
     		#mstdfilename = file.filename
   
		print(mstdfilename)
      
		stdmcqdestination = "/".join([target, mstdfilename])
		print("Accept incoming file:", mstdfilename)
		print(stdmcqdestination)
		file.save(stdmcqdestination)
	return render_template('check2.html',mcqpaper=mcqpaper,mstdfilename=mstdfilename,username = fullname)

@app.route("/uploadteacher", methods=["POST"])
def uploadteacher():
	global mteafilename
	global teamcqdestination
	target = "C:/Users/Areeba Aftab/Desktop/checker/flask"
   #target = os.path.join(APP_ROOT,'/teachermcq')
 
	print(target)
	if not os.path.isdir(target):
		os.mkdir(target)

	for file in request.files.getlist("mcqtea_file"):
		print(file)

		mteafilename = file.filename
		teamcqdestination = "/".join([target, mteafilename])
		print("Accept incoming file:", mteafilename)
		print(teamcqdestination)
		file.save(teamcqdestination)
	return render_template('check2.html',mcqpaper=mcqpaper,mstdfilename=mstdfilename,mteafilename=mteafilename,username = fullname)
@app.route("/omr")
def omr():
	print("student is "+stdmcqdestination)
	print("teacher is "+teamcqdestination)
	print("Paper is "+mcqpaper)
	print("full name is "+fullname)
	global rollno
	filepath=(os.path.splitext(mstdfilename)[0])
	rollno=os.path.basename(filepath)
	print("Rollno is",rollno)
	a=stdmcqdestination
	b=teamcqdestination
	image1 = cv2.imread(a)
	gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
	blurred1 = cv2.GaussianBlur(gray1, (5, 5), 0)
	edged1 = cv2.Canny(blurred1, 75, 200)
	image2 = cv2.imread(b)
	gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
	blurred2 = cv2.GaussianBlur(gray2, (5, 5), 0)
	edged2 = cv2.Canny(blurred2, 75, 200)
    		# find contours in the edge map, then initialize
    		# the contour that corresponds to the document
	cnts1 = cv2.findContours(edged1.copy(), cv2.RETR_EXTERNAL,
    			 cv2.CHAIN_APPROX_SIMPLE)
	cnts1 = cnts1[0] if imutils.is_cv2() else cnts1[1]
	docCnt1 = None
	cnts2 = cv2.findContours(edged2.copy(), cv2.RETR_EXTERNAL,
    			cv2.CHAIN_APPROX_SIMPLE)
	cnts2 = cnts2[0] if imutils.is_cv2() else cnts2[1]
	docCnt2 = None
    		# ensure that at least one contour was found
	if len(cnts1) > 0:
        
    			# sort the contours according to their size in
    			# descending order
		cnts1 = sorted(cnts1, key=cv2.contourArea, reverse=True)
	 
		# loop over the sorted contours
		for c1 in cnts1:
			# approximate the contour
			peri1 = cv2.arcLength(c1, True)
			approx1 = cv2.approxPolyDP(c1, 0.02 * peri1, True)
	 
			# if our approximated contour has four points,
			# then we can assume we have found the paper
			if len(approx1) == 4:
				docCnt1 = approx1
				break
	if len(cnts2) > 0:
    			# sort the contours according to their size in
    			# descending order
		cnts2 = sorted(cnts2, key=cv2.contourArea, reverse=True)
	 
		# loop over the sorted contours
		for c2 in cnts2:
			# approximate the contour
			peri2 = cv2.arcLength(c2, True)
			approx2 = cv2.approxPolyDP(c2, 0.02 * peri2, True)
	 
			# if our approximated contour has four points,
			# then we can assume we have found the paper
			if len(approx2) == 4:
				docCnt2 = approx2
				break
    		# apply a four point perspective transform to both the
    		# original image and grayscale image to obtain a top-down
    		# birds eye view of the paper
	paper1 = four_point_transform(image1, docCnt1.reshape(4, 2))
	warped1 = four_point_transform(gray1, docCnt1.reshape(4, 2))
	paper2 = four_point_transform(image2, docCnt2.reshape(4, 2))
	warped2 = four_point_transform(gray2, docCnt2.reshape(4, 2))
    		# apply Otsu's thresholding method to binarize the warped
    		# piece of paper
	thresh1 = cv2.threshold(warped1, 0, 255,
    			cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
	thresh2 = cv2.threshold(warped2, 0, 255,
    			cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    		# find contours in the thresholded image, then initialize
    		# the list of contours that correspond to questions
	cnts1 = cv2.findContours(thresh1.copy(), cv2.RETR_EXTERNAL,
    			cv2.CHAIN_APPROX_SIMPLE)
	cnts1 = cnts1[0] if imutils.is_cv2() else cnts1[1]
	questionCnts1 = []
	cnts2 = cv2.findContours(thresh2.copy(), cv2.RETR_EXTERNAL,
    			cv2.CHAIN_APPROX_SIMPLE)
	cnts2 = cnts2[0] if imutils.is_cv2() else cnts2[1]
	questionCnts2 = []
    		# loop over the contours
	for c1 in cnts1:
    			# compute the bounding box of the contour, then use the
    			# bounding box to derive the aspect ratio
		(x1, y1, w1, h1) = cv2.boundingRect(c1)
		ar1 = w1 / float(h1)
	 
		# in order to label the contour as a question, region
		# should be sufficiently wide, sufficiently tall, and
		# have an aspect ratio approximately equal to 1
		if w1 >= 20 and h1 >= 20 and ar1 >= 0.9 and ar1 <= 1.1:
			questionCnts1.append(c1)
	for c2 in cnts2:
    			# compute the bounding box of the contour, then use the
    			# bounding box to derive the aspect ratio
		(x2, y2, w2, h2) = cv2.boundingRect(c2)
		ar2 = w2 / float(h2)
	    # in order to label the contour as a question, region
		# should be sufficiently wide, sufficiently tall, and
		# have an aspect ratio approximately equal to 1
		if w2 >= 20 and h2 >= 20 and ar2 >= 0.9 and ar2 <= 1.1:
			questionCnts2.append(c2)
    		# sort the question contours top-to-bottom, then initialize
    		# the total number of correct answers
	questionCnts1 = contours.sort_contours(questionCnts1,
    			method="top-to-bottom")[0]
	correct = 0
	questionCnts2 = contours.sort_contours(questionCnts2,
    			method="top-to-bottom")[0]
            # each question has 5 possible answers, to loop over the
    		# question in batches of 5
	for (q1, i1) in enumerate(np.arange(0, len(questionCnts1), 5)):
    			# sort the contours for the current question from
    			# left to right, then initialize the index of the
    			# bubbled answer
		cnts1 = contours.sort_contours(questionCnts1[i1:i1 + 5])[0]
		bubbled1 = None
		cnts2 = contours.sort_contours(questionCnts2[i1:i1 + 5])[0]
		bubbled2 = None
	# loop over the sorted contours
		for (j1, c1) in enumerate(cnts1):
			for(j2,c2) in enumerate(cnts2):
				mask1 = np.zeros(thresh1.shape, dtype="uint8")
				cv2.drawContours(mask1, [c1], -1, 255, -1)
				mask2 = np.zeros(thresh2.shape, dtype="uint8")
				cv2.drawContours(mask2, [c2], -1, 255, -1)
	           # apply the mask to the thresholded image, then
	#    		# count the number of non-zero pixels in the
	#    		# bubble area
				mask1 = cv2.bitwise_and(thresh1, thresh1, mask=mask1)
				total1 = cv2.countNonZero(mask1)
				mask2 = cv2.bitwise_and(thresh2, thresh2, mask=mask2)
				total2 = cv2.countNonZero(mask2)
	            # if the current total has a larger number of total
	#    		# non-zero pixels, then we are examining the currently
	#    		# bubbled-in answer
				if bubbled1 is None or total1 > bubbled1[0]:
					bubbled1 = (total1, j1)
				if bubbled2 is None or total2 > bubbled2[0]:
					bubbled2 = (total2, j2)
	    # initialize the contour color and the index of the
	    	# *correct* answer
		color = (0, 0, 255)
		k =bubbled2[1]
	    # check to see if the bubbled answer is correct
		if k == bubbled1[1]:
			color = (0, 255, 0)
			correct += 1
	# draw the outline of the corr2ect answer on the test
		cv2.drawContours(paper1, [cnts1[k]], -1, color, 3)
    		
	score = (correct / 5.0) * 100
	print("[INFO] score: {:.2f}%".format(score))
	cv2.putText(paper1, "{:.2f}%".format(score), (10, 30),
    			cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
	cv2.imshow("Teacher", image2)
	cv2.imshow("Exam", paper1)
	cv2.waitKey(0)
	conn=psycopg2.connect("dbname=checker user=postgres password=areeba host=localhost")
	cur=conn.cursor()
	# cur.execute("INSERT INTO std (paper_id,q_id,marks_of_ques,total_marks) SELECT paper_id,q_id,marks_of_q,total_marks FROM question q WHERE q.paper_name = %s",(mcqpaper,))
	
	# cur.execute("INSERT INTO std (paper_id,q_id,marks_of_ques,total_marks) SELECT paper_id,q_id,marks_of_q,total_marks FROM question q WHERE q.paper_name = %s",(mpaper,))
	# conn.commit()
	session['student'] = session.get('student',0)

	session['student']+=1

	cur.execute("SELECT userid from userinfo where name=%s",(fullname,))
	rows=cur.fetchall()
	uid=rows[0]
	print(uid)
	cur.execute("SELECT paper_id from paper where paper_name=%s AND userid=%s",(mpaper,uid))
	rows=cur.fetchall()
	pid=rows[0]
	cur.execute("INSERT INTO stdinfo(std_rollnum) VALUES(%s)",(rollno,))
	conn.commit()
	cur.execute("SELECT std_id FROM stdinfo WHERE std_rollnum = %s",(rollno,))
	rows=cur.fetchall()
	stdid=rows[0]
	# cur.execute("Select count(*) from(SELECT paper_id,q_id,marks_of_q,total_marks FROM question q WHERE q.paper_name = %s AND q.paper_name=%s)stdnew",(mcqpaper,mpaper)) 
	# quesrow=cur.fetchall()
	# quesrow_len=quesrow[0][0]
	# print(quesrow_len)
	# for i in range(quesrow_len):
	# 	cur.execute("INSERT INTO std(std_id,std_rollnum) VALUES(%s,%s)",(stdid,rollno,))
	# 	conn.commit()
	cur.execute("INSERT INTO std (paper_id,q_id,marks_of_ques,total_marks,std_id,std_rollnum,obt_marks_of_ques) SELECT paper_id,q_id,marks_of_q,total_marks,%s,%s,%s FROM question q WHERE q.paper_name = %s ",(stdid,rollno,correct,mpaper,))
	conn.commit()
	# cur.execute("UPDATE std SET paper_id= (Select paper_id from question WHERE paper_name = %s,(mcqpaper,)),q_id= (Select q_id from question WHERE paper_name = %s,(mcqpaper,)) ,marks_of_ques= (Select marks_of_q from question WHERE paper_name = %s,(mcqpaper,)),total_marks=(Select total_marks from question WHERE paper_name = %s,(mcqpaper,)) WHERE std_rollnum=%s ", (rollno, pid))
	# conn.commit()
	
	return redirect(url_for('check'))

@app.route("/thuploadstudent", methods=["POST"])
def thuploadstudent():
	global thpaper
	global thstdfilename
	global stdthdestination
	global thstdtarget
	thpaper = request.form.get('th_paper')
	thstdtarget = os.path.join(APP_ROOT,'/stdtheory')
	print(thstdtarget)
	if not os.path.isdir(thstdtarget):
		os.mkdir(thstdtarget)

	for file in request.files.getlist("thstd_file"):
		print(file)

		thstdfilename = file.filename
		print(thstdfilename)
		stdthdestination = "/".join([thstdtarget, thstdfilename])
		print("Accept incoming file:", thstdfilename)
		print(stdthdestination)
		file.save(stdthdestination)
	return render_template('check3.html',thpaper=thpaper,thstdfilename=thstdfilename,username = fullname)

@app.route("/thuploadteacher", methods=["POST"])
def thuploadteacher():
	global thteafilename
	global teathdestination
	target = os.path.join(APP_ROOT, '/teachertheory')
	print(target)
	if not os.path.isdir(target):
		os.mkdir(target)

	for file in request.files.getlist("thtea_file"):
		print(file)

		thteafilename = file.filename
		teathdestination = "/".join([target, thteafilename])
		print("Accept incoming file:", thteafilename)
		print(teathdestination)
		file.save(teathdestination)
	return render_template('check3.html',thpaper=thpaper,thstdfilename=thstdfilename,thteafilename=thteafilename,username = fullname)	

@app.route('/deffile')
def definition_file():
	# teathdestination+" student folder is "+thstdtarget
	print("Teacher file: "+teathdestination)
	print("Student folder is "+thstdtarget)
	print("Student file: "+stdthdestination)
	global obtmarks1
	global obtacc1
	global obtmarks2
	global obtacc2
	global obtmarks3
	global obtacc3
	stop_words = set(stopwords.words("english"))

	lookup = "What is computer?"
	lookup2= "What is the difference between Internet and Intranet?"
	lookup3= "What is an operating system? Also give some Examples?"


	with open(teathdestination, 'r') as myFile:
		
		for num, line in enumerate(myFile, 0):
			
			if lookup in line:

				print('found at line:', num)
				a=num
			if lookup2 in line:
				print('found at line:', num)
				b=num
			if lookup3 in line:
				print('found at line:', num)
				d=num
		e=num
    #print(num)
		c= teathdestination               
		with open(c,'r') as myfile:

			raw_documents=myfile.readlines()[a+1:b]
        #print(raw_documents)
        #print("Number of documents:",len(raw_documents))
			raw_documents = [''.join(a for a in s if a not in string.punctuation) for s in raw_documents]
        #print(raw_documents)
			AllWords = list()      #create new list
			ResultList = list()
			for line in raw_documents:
				line.rstrip()   #strip white space
				words = line.split()    #split lines of words and make list
				AllWords.extend(words)   #make the list from 4 lists to 1 list
    
			AllWords.sort()  #sort list
    
			for word in AllWords:   #for each word in line.split()
				if word not in ResultList:
				    #if a word isn't in line.split            
					ResultList.append(word)   #append it.
        #print(ResultList)
        
			gen_docs = [w.lower() for w in ResultList if w not in stop_words]
			a=[]
			for i in gen_docs:
				q=nltk.pos_tag(gen_docs)
				for i in range(len(q)):
                
					if q[i][1]=='RB':

						for ss in wn.synsets(q[i][0], pos=wn.ADV):

                        #print(ss, ss.definition())
							a=a+[ss.definition()]
					elif q[i][1]=='NN' or q[i][1]=='NNS' or q[i][1]=='NNP':
						for ss in wn.synsets(q[i][0], pos=wn.NOUN):
                         
                        #print(ss, ss.definition())
							a=a+[ss.definition()]
					elif q[i][1]=='JJ':
						for ss in wn.synsets(q[i][0], pos=wn.ADJ):
                         #print(ss, ss.definition())
							a=a+[ss.definition()]
					elif q[i][1]=='VB':
						for ss in wn.synsets(q[i][0], pos=wn.VERB):
                         #print(ss, ss.definition())
							 a=a+[ss.definition()]


			AllWords = list()      #create new list
			ResultList = list()
			for line in a:

				line.rstrip()   #strip white space
				words = line.split()    #split lines of words and make list
				AllWords.extend(words)   #make the list from 4 lists to 1 list

			AllWords.sort()  #sort list

			for word in AllWords:   #for each word in line.split()
				if word not in ResultList:
					ResultList.append(word)   #append it.
	        #print(ResultList)
			ResultListt=gen_docs+ResultList
	        
			gen_docs = [[w.lower() for w in word_tokenize(word) if w not in stop_words] 
	                        for word in ResultListt]
	        
	        #print(gen_docs)
			dictionary1 = gensim.corpora.Dictionary(gen_docs)
	        #print(dictionary[2])
	#print(dictionary.token2id['road'])
	        #print("Number of words in dictionary1:",len(dictionary1))
			for i in range(len(dictionary1)):
	              #print(i, dictionary1[i])
				corpus1 = [dictionary1.doc2bow(gen_doc) for gen_doc in gen_docs]
	        #print(corpus1)

			tf_idf1 = gensim.models.TfidfModel(corpus1)
	        #print(tf_idf1)
			s = 0
			for i in corpus1:
				s += len(i)
	        #print(s)
			sims1 = gensim.similarities.Similarity(teathdestination,tf_idf1[corpus1],
	                                              num_features=len(dictionary1))
			print(sims1)
	    
		c= teathdestination                 
		with open(c,'r') as myfile:

			raw_documents=myfile.readlines()[b+1:d]
	        #print(len(raw_documents))
	        #print("Number of documents:",len(raw_documents))
			raw_documents = [''.join(a for a in s if a not in string.punctuation) for s in raw_documents]
	        #print(raw_documents)
			AllWords = list()      #create new list
			ResultList = list()
			for line in raw_documents:

				line.rstrip()   #strip white space
				words = line.split()    #split lines of words and make list
				AllWords.extend(words)   #make the list from 4 lists to 1 list
	    
			AllWords.sort()  #sort list
	    
			for word in AllWords:  #for each word in line.split()
				if word not in ResultList:
					ResultList.append(word)   #append it.
	        #print(ResultList)
	        
			gen_docs = [w.lower() for w in ResultList if w not in stop_words]
			a=[]
			for i in gen_docs:
				q=nltk.pos_tag(gen_docs)
				for i in range(len(q)):
	                
					if q[i][1]=='RB':

						for ss in wn.synsets(q[i][0], pos=wn.ADV):
							a
	                        #print(ss, ss.definition())
							a=a+[ss.definition()]
					elif q[i][1]=='NN' or q[i][1]=='NNS' or q[i][1]=='NNP':
						for ss in wn.synsets(q[i][0], pos=wn.NOUN):
	                         
	                        #print(ss, ss.definition())
							a=a+[ss.definition()]
					elif q[i][1]=='JJ':
						for ss in wn.synsets(q[i][0], pos=wn.ADJ):
	                         #print(ss, ss.definition())
							a=a+[ss.definition()]
					elif q[i][1]=='VB':
						for ss in wn.synsets(q[i][0], pos=wn.VERB):
	                         #print(ss, ss.definition())
							a=a+[ss.definition()]


			AllWords = list()      #create new list
			ResultList = list()
			for line in a:

				line.rstrip()   #strip white space
				words = line.split()    #split lines of words and make list
				AllWords.extend(words)   #make the list from 4 lists to 1 list

			AllWords.sort()  #sort list

			for word in AllWords:   #for each word in line.split()
				if word not in ResultList: 
					ResultList.append(word)   #append it.
	        #print(ResultList)
			ResultListt=gen_docs+ResultList
			gen_docs = [[w.lower() for w in word_tokenize(word) if w not in stop_words] 
	                       for word in ResultListt]
	        
	        #print(gen_docs2)
			dictionary2 = gensim.corpora.Dictionary(gen_docs)
	        #print(dictionary[2])
	#print(dictionary.token2id['road'])
	        #print("Number of words in dictionary2:",len(dictionary2))
			for i in range(len(dictionary2)):
				print(i, dictionary2[i])
				corpus2 = [dictionary2.doc2bow(gen_doc) for gen_doc in gen_docs]
	        #print(corpus2)

			tf_idf2 = gensim.models.TfidfModel(corpus2)
	        #print(tf_idf2)
			s = 0
			for i in corpus2:
				s += len(i)
	        #print(s)
			sims2 = gensim.similarities.Similarity(teathdestination,tf_idf2[corpus2],
	                                                  num_features=len(dictionary2))
			print(sims2)
		c= teathdestination                
		with open(c,'r') as myfile:

			raw_documents=myfile.readlines()[d+1:e]
	        #print(raw_documents)
			raw_documents = [''.join(a for a in s if a not in string.punctuation) for s in raw_documents]
	        #print(raw_documents)
			AllWords = list()      #create new list
			ResultList = list()
			for line in raw_documents:

				line.rstrip()   #strip white space
				words = line.split()    #split lines of words and make list
				AllWords.extend(words)   #make the list from 4 lists to 1 list
	    
			AllWords.sort()  #sort list
	    
			for word in AllWords:   #for each word in line.split()
				if word not in ResultList:
					ResultList.append(word)   #append it.
	        #print(ResultList)
	        
			gen_docs = [w.lower() for w in ResultList if w not in stop_words]
			a=[]
			for i in gen_docs:
				q=nltk.pos_tag(gen_docs)
				for i in range(len(q)):
	                
					if q[i][1]=='RB':

						for ss in wn.synsets(q[i][0], pos=wn.ADV):

	                        #print(ss, ss.definition())
							a=a+[ss.definition()]
					elif q[i][1]=='NN' or q[i][1]=='NNS' or q[i][1]=='NNP':
						for ss in wn.synsets(q[i][0], pos=wn.NOUN):
	                         
	                        #print(ss, ss.definition())
							a=a+[ss.definition()]
					elif q[i][1]=='JJ':
						for ss in wn.synsets(q[i][0], pos=wn.ADJ):
	                         #print(ss, ss.definition())
							a=a+[ss.definition()]
					elif q[i][1]=='VB':
						for ss in wn.synsets(q[i][0], pos=wn.VERB):
	                         #print(ss, ss.definition())
							a=a+[ss.definition()]


			AllWords = list()      #create new list
			ResultList = list()
			for line in a:
				line.rstrip()   #strip white space
				words = line.split()    #split lines of words and make list
				AllWords.extend(words)   #make the list from 4 lists to 1 list

			AllWords.sort()  #sort list

			for word in AllWords:   #for each word in line.split()
				if word not in ResultList:    #if a word isn't in line.split            
					ResultList.append(word)   #append it.
	        #print(ResultList)
			ResultListt=gen_docs+ResultList
			gen_docs = [[w.lower() for w in word_tokenize(word) if w not in stop_words] 
	                      for word in ResultListt]
	        
			print(gen_docs)
			dictionary3 = gensim.corpora.Dictionary(gen_docs)
	        
	#print(dictionary.token2id['road'])
	        #print("Number of words in dictionary3:",len(dictionary3))
			for i in range(len(dictionary3)):
				print(i, dictionary3[i])
				corpus3 = [dictionary3.doc2bow(gen_doc) for gen_doc in gen_docs]
	        #print(corpus3)

			tf_idf3 = gensim.models.TfidfModel(corpus3)
	        
	        #print(tf_idf3)
			s = 0
			for i in corpus3:
				s += len(i)
	        #print(s)
			sims3 = gensim.similarities.Similarity(teathdestination,tf_idf3[corpus3],
	                                                   num_features=len(dictionary3))
	        #print(sims3)
	            
	#MAIN CODE
	#a= "answersheet/answersheet1.txt" 
	#myfile= open(a, 'r')
	#raw_documents=myfile.readlines()
	#print(raw_documents)
	#print("Number of documents:",len(raw_documents))
	#stop_words = set(stopwords.words("english"))
	#gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stop_words] 
	#                for text in raw_documents]
	#dictionary = gensim.corpora.Dictionary(gen_docs)
	#print(dictionary[2])
	##print(dictionary.token2id['road'])
	#print("Number of words in dictionary:",len(dictionary))
	#for i in range(len(dictionary)):
	#    print(i, dictionary[i])
	#    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
	#print(corpus)
	#
	#tf_idf = gensim.models.TfidfModel(corpus)
	#print(tf_idf)
	#s = 0
	#for i in corpus:
	#    s += len(i)
	#print(s)
	#sims = gensim.similarities.Similarity('gensimfile2.txt',tf_idf[corpus],
	#                                      num_features=len(dictionary))
	#print(sims)
	#print(type(sims))
	#
	#inputdir = "papers/"
	#filelist = os.listdir(inputdir)

	#ORIGINAL ACCURACIES
	marks1=5
	marks2=2
	marks3=5        
	lookup = "What is computer?"
	lookup2= "What is the difference between Internet and Intranet?"
	lookup3= "What is an operating system? Also give some Examples?"
	c= teathdestination                
	with open(c, 'r') as myFile:
	    for num, line in enumerate(myFile, 0):
	        if lookup in line:
	            print('found at line:', num)
	            a=num
	            l=a+1
	        if lookup2 in line:
	            print('found at line:', num)
	            b=num
	            m=b+1
	        if lookup3 in line:
	            print('found at line:', num)
	            d=num
	    e=num+1      
	    
	    c= teathdestination               
	    with open(c,'r') as myfile:
	         z=b-l
	         lines=myfile.readlines()[a+1:b]
	         lines = [''.join(a for a in s if a not in string.punctuation) for s in lines]
	         q=[]
	         AllWords = list()      #create new list
	         ResultList = list()
	         for line in lines:
	             line.rstrip()   #strip white space
	             words = line.split()    #split lines of words and make list
	             AllWords.extend(words)   #make the list from 4 lists to 1 list

	         AllWords.sort()  #sort list

	         for word in AllWords:   #for each word in line.split()
	               if word not in ResultList:    #if a word isn't in line.split            
	                     ResultList.append(word)   #append it.
	         #print(ResultList)
	             #query_doc = [w.lower() for w in word_tokenize(line) if w not in stop_words]
	             #print(query_doc)
	         query_doc = [w.lower() for w in ResultList if w not in stop_words]
	         query_doc_bow = dictionary1.doc2bow(query_doc)
	        #print(query_doc_bow)
	         query_doc_tf_idf = tf_idf1[query_doc_bow]
	         #print(query_doc_tf_idf)
	         #q= q+sims1[query_doc_tf_idf]
	         a=sims1[query_doc_tf_idf]
	         #print(sims1[query_doc_tf_idf])

	                #a= a.round()
	         #print([a[i] for i, e in enumerate(a) if a[i] !=0])                     
	         q=[a[i] for i, e in enumerate(a) if e != 0]  
	         acc1=sum(q) 
	         print(acc1)
	         
	    c= teathdestination                 
	    with open(c,'r') as myfile:
	        lines=myfile.readlines()[b+1:d]
	        #print(lines)
	            
    
            

