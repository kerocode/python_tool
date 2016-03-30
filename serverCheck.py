
"""
 This is a web connection testing program that uses sys and optparse
 to parse command line arguments
"""


import httplib, sys
from optparse import OptionParser

usageString = "Usage: %prog [options] hostname"
parser = OptionParser( usage=usageString )
parser.add_option("-p", "--port", dest="port", metavar="PORT",
	default=80, type="int", help="Port to connect to")
	
(opts,args) = parser.parse_args()

if len(args) < 1:
	parser.error("Hostname is required")
	
host = args[0]
port = opts.port
client = httplib.HTTPConnection(host,port)
client.request("GET", "/")
resp = client.getresponse()
client.close()

if resp.status == 200:
		print host + " : OK"
		sys.exit()
	
print host + " : DOWN! (" + str(resp.status) + " , " + str(resp.reason) + ")"
