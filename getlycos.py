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
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import sys
import DBkeywords
import test_DB
import currentdate
import getextraweb
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
	page_source =browser.page_source
	soup = BeautifulSoup(page_source,"lxml")
	[s.extract() for s in soup('script')]
	ID =DBkeywords.findkeywordID(keyword)
	resultofitems = soup.find_all("div",{"class":"results search-results"})
	while resultofitems==None :
		time.sleep(20)
		print "searching page cannot load"
		browser.quit()
		browser = get_browser(binary=firefox_binary)
		browser.get(url)
		soup = BeautifulSoup(page_source,"lxml")
		[s.extract() for s in soup('script')]
		resultofitems = soup.find_all("div",{"class":"results search-results"})
	for lycossucks in resultofitems:
		lycossucker = lycossucks.find_all("li",{"class":"result-item"})
		for item in lycossucker:
			try:
				# abstract = element.find("span",{"class":"st"}).get_text()
				Tittle = item.find("h2",{"class":"result-title"}).get_text()
				further_url ='cannot load url'
				further_url = item.find("span",{"class":"result-url"}).get_text()
				abstract = item.find("span",{"class":"result-description"}).get_text()
				if(DBkeywords.checktrustful(further_url)):
					print "trust url:"+str(further_url)
					continue
				print "working on:"+further_url
				browser.set_page_load_timeout(180)	
				browser.get(getextraweb.checkhttp(further_url))
				# try:
				# 	WebDriverWait(browser, 20).until(EC.presence_of_element_located(browser.find_element_by_xpath("*/body")))
				# 	print "Page is ready!"
				# except TimeoutException:
				# 	print "Loading took too much time!"
				body = browser.page_source
				test_DB.lycos(ID[0],Tittle,further_url,abstract,body,currentdate.getdate(),ac)
			except AttributeError:
				print str('AttributeError')
				test_DB.suspect('lycos',-1,ID[0],further_url,3,currentdate.getdate(),'AttributeError',Tittle,abstract)
				continue
			except Exception, e:
				print "caught exception :site:"+further_url +"keyword: "+keyword+" "
				test_DB.suspect('lycos',-1,ID[0],further_url,3,currentdate.getdate(),str(e),Tittle,abstract)
				print str(e)
				continue
	# browser.quit()
if __name__ == "__main__":
	li=DBkeywords.loadsunsearchedkeywords('lycos')
	print li
	count =0
	for l in li:
		# if count>10:
			# break
		try:	
			url = 'http://search.lycos.com/web/?q='+l[0].replace(" ","+")
			get_search(url,l[0],'FR')
			time.sleep(50)
		except Exception, e:
				print str(e)
				continue
		# count +=1
