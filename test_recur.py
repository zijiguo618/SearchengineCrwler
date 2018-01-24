
from bs4 import BeautifulSoup
import time
from time import sleep
import string


def prin():
	print "----------------inside of prin--------------"


def reader(html):
	soup = BeautifulSoup(html,"lxml")
	letters=soup.find_all("li",{"class":"b_algo"})
	print type(letters)

	for element in letters:
		print "Tittle:" + element.a.get_text()
		print "site:" +element.a["href"]
		prin()
		print "abstract:" +element.p.get_text()

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

def formatoutput():
	myfile = open("reduce_trash.txt", "r")
	data = myfile.read().replace('\t','')
	print myfile.read()
	print "----"
	print data.strip()
	print "hello     		worl 	\n	!".replace(' ','')


def testtime():
	
	ctime = time.time()
	sleep(2)
	print ctime
	print time.time()
	
	timedif = time.time()-ctime
	print timedif
	if timedif>2:
		print "it's been 2 more seconds"


def main():
	print "main function in test_recur.py"

if __name__ == "__main__":
	# files =open("log.txt","r")
 #    	f=files.read()
	# reader(f)
	# testtime()
	myfile = open("reduce_trash.txt", "r")
	data = myfile.read()
	formatoutput()
	print cleanup(data)