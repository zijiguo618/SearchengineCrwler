# -*- coding: utf-8 -*-
import os
import io
import time
import string
from time import sleep
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium import webdriver
from lxml import html
import MySQLdb
from xvfbwrapper import Xvfb
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import sys
import DBkeywords
import test_DB
import getextraweb
import currentdate
# path to the firefox binary inside the Tor package
binary = '/Applications/TorBrowser.app/Contents/MacOS/firefox'
if os.path.exists(binary) is False:
	raise ValueError("The binary path to Tor firefox does not exist.")
firefox_binary = FirefoxBinary(binary)
firefoxProfile = FirefoxProfile()
	# only one instance of a browser opens, remove global for multiple instances
firefoxProfile.set_preference('thatoneguydotnet.QuickJava.curVersion', '2.1.0') ## Prevents loading the 'thank you for installing screen'
firefoxProfile.set_preference('thatoneguydotnet.QuickJava.startupStatus.Images', 2) ## Turns images off
firefoxProfile.set_preference('thatoneguydotnet.QuickJava.startupStatus.AnimatedImage', 2) ## Turns animated images off

browser = None
def get_browser(binary=None):
	global browser  
	
	if not browser: 
		browser = webdriver.Firefox(firefox_binary=binary,firefox_profile=firefoxProfile)
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
	page_source =browser.page_source
	soup = BeautifulSoup(page_source,"lxml")
	[s.extract() for s in soup('script')]
	letters=soup.find_all("li",{"class":"b_algo"})
	counserat=0
	ID =DBkeywords.findkeywordID(keyword)
	for element in letters:
		try:
			print str(counserat)
			further_url ='cannot load url'
			ctime = time.time()
			Tittle = element.a.get_text()
			further_url = element.a["href"]
			abstract = element.p.get_text()
			if(DBkeywords.checktrustful(further_url)):
				print "trust url:"+str(further_url)
				continue
			print "working on:"+further_url
			# browser.set_page_load_timeout(120)
			browser.get(getextraweb.checkhttp(further_url))
			# try:
			# 	WebDriverWait(browser, 20).until(EC.presence_of_element_located(browser.find_element_by_xpath("*/body")))
			# 	print "Page is ready!"
			# except TimeoutException:
			# 	print "Loading took too much time!"
			time.sleep(30)
			body = browser.page_source
			test_DB.bing(ID[0],Tittle,further_url,abstract,body,currentdate.getdate(),ac)
			counserat =counserat+1
		# except AttributeError:
		# 	print str('AttributeError')
		# 	# test_DB.suspect('bing',-1,ID[0],further_url,3,currentdate.getdate(),'AttributeError',Tittle,abstract)
		# 	# browser.quit()
		# 	continue
		except Exception, e:
			print str(e)
			# browser.quit()
			test_DB.suspect('bing',-1,ID[0],further_url,3,currentdate.getdate(),str(e),Tittle,abstract)
			continue
	time.sleep(30)
	# browser.quit()

def loadsunsearchedkeywords():
	res = DBkeywords.getunsearchedID('bing')
	for ke in res:
		keywordseearching = DBkeywords.findkeyword(ke)
		url = 'https://www.bing.com/search?q='+keywordseearching[0].replace(" ","+")
		get_search(url,keywordseearching[0],'DE')
		time.sleep(50)


def loadallkeywords(ac):
	res = DBkeywords.getkeyword()
	for ke in res:
		try:
			url = 'https://www.bing.com/search?q='+ke[0].replace(" ","+")
			get_search(url,ke[0],ac)
		except Exception, e:
			print str(e)
			continue

if __name__ == "__main__":
	li=DBkeywords.loadsunsearchedkeywords('bing')
	for l in li:
		try:
			url = 'https://www.bing.com/search?q='+l[0].replace(" ","+")
			get_search(url,l[0],'FR')
		except Exception, e:
			print str(e)
			continue
		



