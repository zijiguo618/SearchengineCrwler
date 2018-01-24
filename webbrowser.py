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
from lxml import etree
import MySQLdb
from pprint import pprint
from xvfbwrapper import Xvfb
from time import sleep
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import sys
import DBkeywords
import test_DB
import currentdate
import getbing
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# sys.setdefaultencoding() does not exist, here!

# path to the firefox binary inside the Tor package
binary = '/Applications/TorBrowser.app/Contents/MacOS/firefox'
if os.path.exists(binary) is False:
	raise ValueError("The binary path to Tor firefox does not exist.")
firefox_binary = FirefoxBinary(binary)

firefoxProfile = FirefoxProfile()
firefoxProfile.set_preference('thatoneguydotnet.QuickJava.curVersion', '2.1.0') ## Prevents loading the 'thank you for installing screen'
firefoxProfile.set_preference('thatoneguydotnet.QuickJava.startupStatus.Images', 2) ## Turns images off
firefoxProfile.set_preference('thatoneguydotnet.QuickJava.startupStatus.AnimatedImage', 2) ## Turns animated images off
firefoxProfile.set_preference("thatoneguydotnet.QuickJava.startupStatus.CSS", 2)  ## CSS
firefoxProfile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Cookies", 2)  ## Cookies
firefoxProfile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Flash", 2)  ## Flash
firefoxProfile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Java", 2)  ## Java
firefoxProfile.set_preference("thatoneguydotnet.QuickJava.startupStatus.JavaScript", 2)  ## JavaScript
firefoxProfile.set_preference("thatoneguydotnet.QuickJava.startupStatus.Silverlight", 2)

browser = None
def get_browser(binary=None,profile=None):
	global browser  
	# only one instance of a browser opens, remove global for multiple instances
	# only one instance of a browser opens, remove global for multiple instances
	if not browser: 
		browser = webdriver.Firefox(firefox_profile=firefoxProfile,firefox_binary=binary)
	return browser


def openintab(driver,url):
	browser.execute_script('''window.open("http://bings.com""","_blank");''')
	windows = browser.window_handles
	browser.switch_to.window(windows[1])
	browser.close()







if __name__ == "__main__":
	reload(sys)  # Reload does the trick!
	sys.setdefaultencoding('UTF8')
	url = 'https://www.bing.com/search?q=火龙果'
	browser = get_browser(binary=firefox_binary)
	# browser=webdriver.Firefox(firefoxProfile)
	browser.get(url)
	# browser.implicitly_wait(20)
		# driver.find_element_by_xpath("//div[@id='a']//a[@class='click']")
	time.sleep(5)
	

	urls =browser.find_element_by_xpath("*/body")
	# browser.execute_script("window.open('https://www.iastate.edu', '_blank')")
	# time.sleep(10)
	# print urls.get_attribute("href")
	# windows = browser.window_handles
# 	try:
#     WebDriverWait(browser, delay).until(EC.presence_of_element_located(browser.find_element_by_tag_name('body')))
#     print "Page is ready!"
# except TimeoutException:
#     print "Loading took too much time!"	browser.switch_to.window(windows[1])
# 	# soupfurther = BeautifulSoup(browser.page_source,"lxml")
# 	body = browser.find_element_by_tag_name("body").get_attribute('innerHTML')
	print str(urls)
	# 	print i.get_attribute("href")
	# for i in urls:
	# 	print i.get_attribute("href")
