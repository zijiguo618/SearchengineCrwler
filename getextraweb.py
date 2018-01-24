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
from xvfbwrapper import Xvfb
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import MySQLdb
import sys
import currentdate
import DBkeywords
import test_DB
# path to the firefox binary inside the Tor package
binary = '/Applications/TorBrowser.app/Contents/MacOS/firefox'
if os.path.exists(binary) is False:
	raise ValueError("The binary path to Tor firefox does not exist.")
firefox_binary = FirefoxBinary(binary)
firefoxProfile = FirefoxProfile()
firefoxProfile.set_preference('thatoneguydotnet.QuickJava.curVersion', '2.1.0') ## Prevents loading the 'thank you for installing screen'
firefoxProfile.set_preference('thatoneguydotnet.QuickJava.startupStatus.Images', 2) ## Turns images off
firefoxProfile.set_preference('thatoneguydotnet.QuickJava.startupStatus.AnimatedImage', 2) ## Turns animated images off

browser = None
def get_browser(binary=None,profile=None):
	global browser  
	# only one instance of a browser opens, remove global for multiple instances
	# only one instance of a browser opens, remove global for multiple instances
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

def checkhttp(url):
	if(url.startswith('https://') or url.startswith('http://')):
		return url
	else:
		return 'http://'+url
def baidufurthersearch(url):
	print "getextraweb:"+url
	currenturl =url
	try:
		browser = get_browser(binary=firefox_binary)
		print url
		# browser.get(checkhttp(url))
		browser.get(url)
		page_source =browser.page_source
		currenturl = browser.current_url
		soup = BeautifulSoup(page_source,"lxml")
		[s.extract() for s in soup('script')]
		body = cleanup(soup.get_text())
		browser.quit()
	except AttributeError:
		print str(AttributeError)
		test_DB.suspect('baidu',-1,ID[0],currenturl,3,currentdate.getdate(),'AttributeError',Tittle,abstract)
		# browser.quit()
		# sys.exit()
	except Exception, e:
		print "caught exception :site:"+currenturl +"keyword: "+keyword
		test_DB.suspect('baidu',-1,ID[0],currenturl,3,currentdate.getdate(),str(e),Tittle,abstract)
		print str(e)
		# browser.quit()
		# sys.exit()
	return body

def get_search(url):
	browser = get_browser(binary=firefox_binary)
	print url
	browser.get(checkhttp(url))
	page_source =browser.page_source
	soup = BeautifulSoup(page_source,"lxml")
	[s.extract() for s in soup('script')]
	body = cleanup(soup.get_text())
	browser.Dispose()
	return body