import time
import datetime

def getdate():
	ts = time.time()    
	timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	return timestamp