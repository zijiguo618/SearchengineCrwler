import getbing
import getbaidu
import getgoogle
import DBkeywords
import getsearch
import getaol
import getask
import getlycos

if __name__ == "__main__":
	# res = DBkeywords.getkeyword()
	# li =[]
	# for ke in res:
	# 	# url = 'https://www.bing.com/search?q='+ke[0].replace(" ","+")
	# 	# getbing.get_search(url,ke[0],'FR')
	# 	# url = 'https://www.baidu.com/s?ie=utf-8&wd='+ke[0].replace(" ","+")
	# 	# getbaidu.get_search(url,ke[0])
	# 	# url ='https://www.google.com/search?q='+ke[0].replace(" ","+")
	# 	# getgoogle.get_search(url,ke[0])
	# 	# url ='http://www.ask.com/web?q='
	# 	# https://www.search.com/web?q=search
	# 	# http://search.lycos.com/web/?q=tianzhen
	# 	# http://www.ask.com/web?q=
	# 	url = 'https://search.aol.com/aol/search?s_it=sb-top&v_t=na&q='+ke[0].replace(" ","+")
	# 	getaol.get_search(url,ke[0],'FR')
	getbing.loadallkeywords('US')