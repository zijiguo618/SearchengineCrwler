#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
import time
import datetime
# Open database connection
db = MySQLdb.connect(host="localhost", user="root", passwd="password",
db="sys",charset ='utf8',use_unicode=True)
cursor = db.cursor()

def suspect(engine,engine_id,ID,site,score,cdate,message,tittle,abstract):
	print "hello suspect"
	try:
		cursor.execute ("""INSERT INTO suspect (engine,engine_id,ID,site,score,date,message,tittle,abstract) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(engine,engine_id,ID,site,score,cdate,message,tittle,abstract))
		db.commit()
	except:
		db.rollback()
def search(ID,tittle,site,abstract,html,cdate,ac):
	try:
		print "hello search"
		cursor.execute ("""INSERT INTO search (ID,tittle,site,abstract,html,date,ac)VALUES(%s,%s,%s,%s,%s,%s,%s)""",(ID,tittle,site,abstract,html,cdate,ac))
		db.commit()
	except:
		db.rollback()
def aol(ID,tittle,site,abstract,html,cdate,ac):
	try:

		print cursor.execute ("""INSERT INTO aol (ID,tittle,site,abstract,html,date,ac)VALUES(%s,%s,%s,%s,%s,%s,%s)""",(ID,tittle,site,abstract,html,cdate,ac))
		db.commit()
	except:
		db.rollback()
def ask(ID,tittle,site,abstract,html,cdate,ac):
	try:

		print cursor.execute ("""INSERT INTO ask (ID,tittle,site,abstract,html,date,ac)VALUES(%s,%s,%s,%s,%s,%s,%s)""",(ID,tittle,site,abstract,html,cdate,ac))
		db.commit()
	except:
		db.rollback()
def lycos(ID,tittle,site,abstract,html,cdate,ac):
	try:

		print cursor.execute ("""INSERT INTO lycos (ID,tittle,site,abstract,html,date,ac)VALUES(%s,%s,%s,%s,%s,%s,%s)""",(ID,tittle,site,abstract,html,cdate,ac))
		db.commit()
	except:
		db.rollback()
def bing(ID,tittle,site,abstract,html,cdate,ac):
	try:

		print cursor.execute ("""INSERT INTO bing (ID,tittle,site,abstract,html,date,ac)VALUES(%s,%s,%s,%s,%s,%s,%s)""",(ID,tittle,site,abstract,html,cdate,ac))
		db.commit()
	except:
		db.rollback()
def google(ID,tittle,site,abstract,html,cdate,ac):
	print "hello google"
	try:
		cursor.execute ("""INSERT INTO google (ID,tittle,site,abstract,html,date,ac) VALUES (%s,%s,%s,%s,%s,%s,%s)""",(ID,tittle,site,abstract,html,cdate,ac))
		db.commit()
	except:
		db.rollback()
def baidu(ID,tittle,site,abstract,html,cdate,ac):
	print "hello baidu"
	cursor = db.cursor()
	try:
		cursor.execute ("""INSERT INTO baidu (ID,tittle,site,abstract,html,date,ac) VALUES (%s,%s,%s,%s,%s,%s,%s)""",(ID,tittle,site,abstract,html,cdate,ac))
		db.commit()
	except:
		db.rollback()