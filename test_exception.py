import os
import io
import time
from time import sleep
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from lxml import html
from pprint import pprint
from xvfbwrapper import Xvfb
from time import sleep
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import sys
# sys.setdefaultencoding() does not exist, here!

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
def insideexceptiom():
    print "inside of exception"
if __name__ == "__main__":
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')
    browser = get_browser(binary=firefox_binary)
    try:
        browser.get("https://www.wellness4life.myzija.com/")
    # except WebDriverException:
    #     print "caught exception" +"WebDriverException"
    #     insideexceptiom()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print message
        insideexceptiom()
    print "congratulations, you caught the exception and arraived here"
        