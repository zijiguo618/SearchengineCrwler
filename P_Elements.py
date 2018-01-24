from bs4 import BeautifulSoup



def reader(html):
	soup = BeautifulSoup(html,"lxml")
	letters=soup.find_all("li",{"class":"b_algo"})
	print type(letters)
	for element in letters:
		print "Tittle:" + element.a.get_text()
		print "site:" +element.a["href"]
		print "abstract:" +element.p.get_text()

if __name__ == "__main__":
	files =open("log.txt","r")
    	f=files.read()
	reader(f)