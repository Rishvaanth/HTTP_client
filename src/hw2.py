
import logging
import socket
import sys
import http.server


def retrieve_url(url):

    print(f"The url is: {url}")

    connectionMode = url[:url.rfind(':')].strip()
    print(connectionMode)
    host = url[url.rfind(':') + 1:].strip()
    print(host)




    return b"this is unlikely to be correct"

if __name__ == "__main__":
    sys.stdout.buffer.write(retrieve_url(sys.argv[1])) # pylint: disable=no-member
