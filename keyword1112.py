# -*- coding: utf-8 -*-
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="password",
db="sys",charset ='utf8',use_unicode=True)

def findkeywordID(keyword):
# prepare a cursor object using cursor() method
	cursor = db.cursor()
# Prepare SQL query to INSERT a record into the database.
	try:
   # Execute the SQL command
   		# cursor.execute("INSERT INTO bing (ID) VALUES(%s)",('2'))
   		cursor.execute ("SELECT ID FROM keyword WHERE keyword =%s",keyword)
   # Commit your changes in the database
   		db.commit()
	except:
   # Rollback in case there is any error
   		db.rollback()
# disconnect from server
	db.close()
	result =cursor.fetchall()
	return result[0]

def loadkeyword():
	print "loading keywords"


