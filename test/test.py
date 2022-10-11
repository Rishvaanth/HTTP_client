# import http.client
# import urllib3
# import requests
#
# url = 'https://www.google.com'
# # response = requests.get(url)
# # if response.status_code == 200:
# #     print(response.content)
# # else:
# #     print(f"Obtained a different output {response.status_code}")
#
# h1 = urllib3.PoolManager()
#
# request = h1.request('GET', url)
# if request.status


import urllib3

url = 'https://www.google.com'
https = urllib3.PoolManager()
request = https.request('GET', url)
if request.status == 200:
    print(request.data)