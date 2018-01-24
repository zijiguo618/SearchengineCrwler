# -*- coding: utf-8 -*-
# coding: utf8
import MySQLdb
import getbing
import currentdate

db = MySQLdb.connect(host="localhost", user="root", passwd="password",
db="sys",charset ='utf8',use_unicode=True)
cursor = db.cursor()

def findkeywordID(inpu):
	# print "finding keyword ID from DB , keyword is:"+inpu
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
	result =cursor.fetchall()
	return result[0]

def findkeyword(inpu):
	# print "finding keyword from DB , ID is:"+str(inpu)
	try:
   # Execute the SQL command
		# cursor.execute("INSERT INTO bing (ID) VALUES(%s)",('2'))
		cursor.execute ("SELECT keyword FROM keyword WHERE ID =%s",[inpu])
   # Commit your changes in the database
		db.commit()
	except MySQLdb.ProgrammingError as ex:
		if cursor:
			print "cursoe exception:"
			print ex
		db.rollback()
	result =cursor.fetchone()
	return result

def getunsearchedID(engine):
	results =[]
	keys =[]
	unsearchedresults =[]
	try:
   # Execute the SQL command
		# cursor.execute("INSERT INTO bing (ID) VALUES(%s)",('2'))
		cursor.execute ("SELECT distinct(ID) FROM "+engine)
   # Commit your changes in the database
		db.commit()
		result =cursor.fetchall()
		for sites in result:
			results.append(sites[0])
		cursor.execute ("SELECT distinct(ID) FROM keyword")
		result = cursor.fetchall()
		for sites in result:
			keys.append(sites[0])
	except MySQLdb.ProgrammingError as ex:
		if cursor:
			print "cursoe exception:"
			print ex
		db.rollback()
	for sites in keys:
		if sites not in results:
			unsearchedresults.append(sites)
	print "done"
	return unsearchedresults

def checktrustful(url):
	# try:
		# print keywords.replace('\n', '')
	cursor.execute ("SELECT website FROM trustfulwebsites")
	db.commit()
	# except Exception,e:
	# 	print str(e)
	# 	print "caught exception in check trustfulwebsites"
	# 	db.rollback()
	result =cursor.fetchall()
	# print result
	for sites in result:
		# print str(sites[0])
		if simplizeurl(str(sites[0])) in url:
			return True
	return False


def simplizeurl(url):
	if(url.startswith("https://")):
		return url[8:len(url)]
	elif(url.startswith("http://")):
		return url[7:len(url)]
	else: 
		return url


# def checkrealurl(url):
# 	if(url.startswith("https://"))return url[8:len(url)]



def loadsunsearchedkeywords(engine):
	res =getunsearchedID(engine)
	li=[]
	for ke in res:
		keywordseearching =findkeyword(ke)
		li.append(keywordseearching)
	return li
		
		

def loadallkeywords():
	res = getkeyword()
	li =[]
	for ke in res:
		li.append(ke[0])
	return li



def loadkeyword():
	# print "loading keywords from local to DB"
	# myfile = open("keywords.txt", "r")
	# myfile.read()
	with open("keywords_1.txt") as f:
		keywordsinput = f.readlines()
	# print keywordsinput[0]
	for keywords in keywordsinput:
		# cursor = db.cursor()
		try:
			# print keywords.replace('\n', '')
			cursor.execute ("INSERT INTO keyword(keyword,date) VALUES(%s,%s)",(keywords.replace('\n', ''),currentdate.getdate()))
			db.commit()
		except Exception,e:
			print str(e)
			print "caught exception:"+keywords.replace('\n', '')+":"+currentdate.getdate()
			db.rollback()

def getkeyword():
	# print "loading keywords from DB"
	try:
		
		cursor.execute ("SELECT keyword FROM keyword")
	except:
		print "caught exception during loading keyword from DB"
		db.rollback()
	result =cursor.fetchall()
	return result


