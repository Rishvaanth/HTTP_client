import logging
import socket
import sys


def retrieve_url(url):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connectionMode = url[:url.find(':')].strip()
    print(connectionMode)
    host = url[url.rfind('//') + 2:].strip()
    print(host)
    sock.connect((host, 80))

    if connectionMode == "https":
        getRequest = "GET /HTTPS/1.1\r\nHost:%s\r\n\r\n" % host
    else:
        getRequest = "GET /HTTP/1.1\r\nHost:%s\r\n\r\n" % host

    sock.sendall(getRequest.encode("utf-8"))
    response = b""
    while True:
        chunk = sock.recv(4096)
        if len(chunk) == 0:
            break
        response = response + chunk
    sock.close()
    return response


if __name__ == "__main__":
    sys.stdout.buffer.write(retrieve_url(sys.argv[1])) # pylint: disable=no-member
