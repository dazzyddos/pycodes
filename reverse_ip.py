# Usage: ./reverse_ip.py <site>
# Example: ./reverse_ip.py facebook.com
import requests
import socket
import sys

site = "http://api.hackertarget.com/reverseiplookup"

if len(sys.argv) != 2:
	print "Usage: reverse_ip.py <site>\n"
	sys.exit(0)

url = sys.argv[1]

ip = socket.gethostbyname(url)
data = {'q':ip}

resp = requests.get(site, params=data)

print resp.text
