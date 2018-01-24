# -*- coding: utf-8 -*-
import os
import io
import time
import string
from time import sleep
from lxml import html
import MySQLdb
from xvfbwrapper import Xvfb
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener
from bs4 import BeautifulSoup
import sys
import DBkeywords
import test_DB
import currentdate
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

def get_search(url):
	browser = get_browser(binary=firefox_binary)
	
	browser.get(url)
	page_source =browser.page_source
	soup = BeautifulSoup(page_source,"lxml")
	[s.extract() for s in soup('script')]
	letters=soup.find_all("li",{"class":"b_algo"})
	
	print type(letters)
	for element in letters:
		browser2 = get_browser(binary=firefox_binary)
		browser2.set_page_load_timeout(1)
		ctime = time.time()
		Tittle = element.a.get_text()
		further_url = element.a["href"]
		print "working on:"+further_url
		abstract = element.p.get_text()
		try:
			browser2.get(further_url)
			soupfurther = BeautifulSoup(browser2.page_source,"lxml")
			[s.extract() for s in soupfurther('script')]
			body = cleanup(soupfurther.get_text())
			print body
		except WebDriverException, e:
			print "caught exception" +"site:"+further_url +"url: "+url
			 # suspect(engine,engine_id,ID,site,score):
			# test_DB.suspect('bing',-1,ID[0],further_url,3,currentdate.getdate())
			continue
