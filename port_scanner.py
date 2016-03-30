from socket import *
import sys
from threading import Thread

host = ''
top_port = 10000
bottom_port = 1

ipAddr = gethostbyname(host)


def start_scan(host, port, r_code = 1):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		
		code = sock.connect_ex((host,port))
		
		if code == 0:
			r_code = 0
		sock.close()
	except Exception, e:
		print e
	return r_code




def singleThreadScan(host,multithread):
	for x in range(bottom_port + multithread,top_port,2):
		try:
			response = start_scan(host, x)
			if response == 0:
				print("Port " + str(x) + " Open")
		except Exception, e:
			print e
			pass
		

def multiThreadScan(host):
	threads = []
	try:
		thread1 = Thread(group=None, target=singleThreadScan, name=None, args=(host, 0), kwargs={})
		threads.append(thread1)
		thread2 = Thread(group=None, target=singleThreadScan, name=None, args=(host, 1), kwargs={})
		threads.append(thread2)
		threads[0].start()
		threads[1].start()
	except Exception, e:
		print e
	for i in threads:
		i.join()

multiThreadScan("127.0.0.1")
		
		
