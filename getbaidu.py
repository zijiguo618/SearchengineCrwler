# -*- coding: utf-8 -*-
import os
import io
import time
import string
from time import sleep
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from lxml import html
import MySQLdb
from xvfbwrapper import Xvfb
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import sys
import DBkeywords
import test_DB
import currentdate
import getextraweb
import thread
# path to the firefox binary inside the Tor package
binary = '/Applications/TorBrowser.app/Contents/MacOS/firefox'
if os.path.exists(binary) is False:
	raise ValueError("The binary path to Tor firefox does not exist.")
firefox_binary = FirefoxBinary(binary)

browser = None
def get_browser(binary=None):
	global browser  
	# only one instance of a browser opens, remove global for multiple instances
	if not browser: 
		browser = webdriver.Firefox(firefox_binary=binary)
	return browser

def cleanup(s, remove=('\n', '\t')):
	newString = ''
	for c in s:
		# Remove special characters defined above.
		# Then we remove anything that is not printable (for instance \xe2)
		# Finally we remove duplicates within the string matching certain characters.
		if c in remove: continue
		elif not c in string.printable: continue
		elif len(newString) > 0 and c == newString[-1] and c in ('\n', ' ', ',', '.'): continue
		newString += c
	return newString

def get_search(url,keyword,ac):
	browser = get_browser(binary=firefox_binary)
	browser.get(url)
	time.sleep(15)
	print "get_search url done"
	page_source =browser.page_source
	soup = BeautifulSoup(page_source,"lxml")
	[s.extract() for s in soup('script')]
	ID =DBkeywords.findkeywordID(keyword)
	resultofitems = soup.find_all("div",{"class":"c-container"})
	print "get_search baidu :"+ url
	# while resultofitems==None :
	# 	print "searching page cannot load"
	# 	WebDriverWait(browser,30)
	# 	browser = get_browser(binary=firefox_binary)
	# 	browser.get(url)
	# 	resultofitems = soup.find_all("div",{"class":"c-container"})
	for item in resultofitems:
		try:
			time.sleep(15)
			Tittle='cannot load '
			abstract='cannot load '
			currenturl ='cannot load url'
			further_url = item.a["href"]
			Tittle = item.a.get_text()
			print Tittle
			abstract = item.find_all("div")[0].get_text()
			print abstract
			# thread.start_new_thread(getextraweb.baidufurthersearch,(ID[0],Tittle,abstract,further_url,ac))
			browser.set_page_load_timeout(180)
			browser.get(further_url)
			try:
				WebDriverWait(browser, 20).until(EC.presence_of_element_located(browser.find_element_by_xpath("*/body")))
				print "Page is ready!"
			except TimeoutException:
				print "Loading took too much time!"
			time.sleep(30)
			currenturl = (browser.current_url)
			print currenturl
			body = browser.page_source
			test_DB.baidu(ID[0],Tittle,currenturl,abstract,body,currentdate.getdate(),ac)
		# except AttributeError:
		# 	print str(AttributeError)
		# 	test_DB.suspect('baidu',-1,ID[0],currenturl,3,currentdate.getdate(),'AttributeError')
		# 	continue
		except TimeoutException, e2:
			print "Timeout, retrying..."
			test_DB.suspect('baidu',-1,ID[0],currenturl,3,currentdate.getdate(),str(e2),Tittle,abstract)
			time.sleep(30)
			continue
		except Exception, e:
			print "caught exception :site:"+currenturl +"keyword: "+keyword
			test_DB.suspect('baidu',-1,ID[0],currenturl,3,currentdate.getdate(),str(e),Tittle,abstract)
			print str(e)
			continue

if __name__ == "__main__":
	# res = DBkeywords.getkeyword()
	res=DBkeywords.loadsunsearchedkeywords('baidu')
	li =[]
	for ke in res:
		url = 'https://www.baidu.com/s?ie=utf-8&wd='+ke[0].replace(" ","+")
		print "main function of baidu :"+ url
		try:
			get_search(url,ke[0],'US')
		except TimeoutException, e:
			print "Timeout, retrying... keyword:"+ke[0]
			time.sleep(30)
			continue
		time.sleep(50)
