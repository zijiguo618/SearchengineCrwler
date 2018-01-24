# -*- coding: utf-8 -*-
import sys
import os
import time
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="password",
db="sys",charset ='utf8',use_unicode=True)
cursor = db.cursor()

def findtrustkeyword(inpu):
	print "finding trustful keyword from DB , keyword is:"+inpu
	try:
   # Execute the SQL command
   		# cursor.execute("INSERT INTO bing (ID) VALUES(%s)",('2'))
   		cursor.execute ("SELECT website FROM trustfulwebsites WHERE keyword =%s",[inpu])
   # Commit your changes in the database
   		db.commit()
	except MySQLdb.ProgrammingError as ex:
		if cursor:
			print "cursoe exception:"
			print ex
   		db.rollback()
	result =cursor.fetchall()
	return result[0]