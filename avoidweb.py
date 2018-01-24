# -*- coding: utf-8 -*-
import MySQLdb
import getbing
import currentdate

db = MySQLdb.connect(host="localhost", user="root", passwd="password",
db="sys",charset ='utf8',use_unicode=True)
cursor = db.cursor()

def findkeywordID(inpu):
	print "finding keyword ID from DB , keyword is:"+inpu
	try:
   # Execute the SQL command
   		# cursor.execute("INSERT INTO bing (ID) VALUES(%s)",('2'))
   		cursor.execute ("SELECT ID FROM keyword WHERE keyword =%s",[inpu])
   # Commit your changes in the database
   		db.commit()
	except MySQLdb.ProgrammingError as ex:
		if cursor:
			print "cursoe exception:"
			print ex
   		db.rollback()
# disconnect from server

	result =cursor.fetchall()
	return result[0]


def checktrustful(url):
	try:
		print keywords.replace('\n', '')
		cursor.execute ("SELECT website FROM trustfulwebsites")
		db.commit()
	except Exception,e:
		print str(e)
		print "caught exception:"+keywords.replace('\n', '')+":"+currentdate.getdate()
		db.rollback()
	result =cursor.fetchall()
	for sites in result:
		if url.find(sites):
			return True
	return False




def loadkeyword():
	print "loading keywords from local to DB"
	# myfile = open("keywords.txt", "r")
	# myfile.read()
	with open("keywords_1.txt") as f:
		keywordsinput = f.readlines()
	# print keywordsinput[0]
	for keywords in keywordsinput:
		# cursor = db.cursor()
		try:
			print keywords.replace('\n', '')
			cursor.execute ("INSERT INTO keyword(keyword,date) VALUES(%s,%s)",(keywords.replace('\n', ''),currentdate.getdate()))
			db.commit()
		except Exception,e:
			print str(e)
			print "caught exception:"+keywords.replace('\n', '')+":"+currentdate.getdate()
			db.rollback()

def getkeyword():
	print "loading keywords from DB"
	try:
		
		cursor.execute ("SELECT keyword FROM keyword")
	except:
		print "caught exception during loading keyword from DB"
		db.rollback()
	result =cursor.fetchall()
	return result
