import logging
import socket
import sys
import requests

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = "http://www.example.com"

connectionMode = url[:url.rfind(':')].strip()
print(f"The connection type is:{connectionMode}")
host = url[url.rfind('/') + 1:].strip()
print(f"The host header is: {host}")

actualResponse = requests.get(url, allow_redirects=False)
print(f"The actual response is: \n \n {actualResponse.content}")
sock.connect((host, 80))
getRequest = "GET / HTTPS/1.1\r\nHost:%s\r\n\r\n" % host
sock.send(getRequest.encode())
response = sock.recv(4096)
http_response = repr(response)
sock.close()
print(f"The full response is: \n \n {http_response}")
