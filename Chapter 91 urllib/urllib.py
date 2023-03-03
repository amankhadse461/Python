import urllib.request
response = urllib.request.urlopen('https://github.com/')
print(response)

print(response.status)

print(response.read())

print(response.read())

#HTTP POST

import urllib
query_parms = {'username':'stackoverflow', 'password':'me.me'}
encoded_parms = urllib.parse.urlencode(query_parms).encode('utf-8')
response = urllib.request.urlopen("https://stackoverflow.com/users/login", encoded_parms)
response.code

response.read()
