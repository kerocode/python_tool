#Thanks to Adam Palmer and his post for Performing DNS queries in Python

import dns.resolver
import dns.zone
import dns.query

theResolver = dns.resolver.Resolver()

#getting A record

def getARecord(hostname):
	return theResolver.query(hostname, "A")
	
def getMXRecord(hostname):
	return theResolver.query(hostname,"MX")
	
def getPTRRecord(ipAddr):
	return theResolver.query('.'.join(reversed(ip.split("."))) + ".in-addr.arpa")
	
getARecord("www.google.com")
	


