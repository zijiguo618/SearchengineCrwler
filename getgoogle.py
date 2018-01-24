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
# path to the firefox binary inside the Tor package
binary = '/Applications/TorBrowser.app/Contents/MacOS/firefox'
if os.path.exists(binary) is False:
	raise ValueError("The binary path to Tor firefox does not exist.")
firefox_binary = FirefoxBinary(binary)
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:53.0) Gecko/20100101 Firefox/53.0

browser = None
def get_browser(binary=None):
	global browser  
	# only one instance of a browser opens, remove global for multiple instances
	if not browser: 
		profile = webdriver.FirefoxProfile()
		profile.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36")
		browser = webdriver.Firefox(firefox_profile=profile,firefox_binary=binary)
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
def get_search(url,keyword):
	browser = get_browser(binary=firefox_binary)
	browser.get(url)
	page_source =browser.page_source
	soup = BeautifulSoup(page_source,"lxml")
	[s.extract() for s in soup('script')]
	letters=soup.find_all("div",{"class":"g"})
	ID =DBkeywords.findkeywordID(keyword)
	for element in letters:
		try:
			ctime = time.time()
			Tittle = element.a.get_text()
			further_url = element.cite.get_text()
			print "working on:"+further_url
			abstract = element.find("span",{"class":"st"}).get_text()
			browser2 = get_browser(binary=firefox_binary)
			browser2.set_page_load_timeout(120)
			browser2.get(further_url)
			soupfurther = BeautifulSoup(browser2.page_source,"lxml")
			[s.extract() for s in soupfurther('script')]
			body = cleanup(soupfurther.get_text())
			test_DB.google(ID[0],Tittle,further_url,abstract,body,currentdate.getdate(),'US')
		except AttributeError:
			print str('AttributeError')
			test_DB.suspect('google',-1,ID[0],further_url,3,currentdate.getdate(),'AttributeError')
			continue
		except Exception, e:
			print str(e)
			test_DB.suspect('google',-1,ID[0],further_url,3,currentdate.getdate(),str(e))
			continue
