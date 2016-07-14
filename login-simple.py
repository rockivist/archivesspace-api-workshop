#!/usr/bin/env python3
import urllib.request
import getpass
    
def login (username, password):
    data = urllib.parse.urlencode({'password': password})
    data = data.encode('ascii')
    req = urllib.request.Request('http://localhost:8089/users/'+username+'/login', data)
    with urllib.request.urlopen(req) as response:
        src = response.read().decode('UTF-8')
    return src

print('Logging in')
s = login(input('ArchivesSpace username: '),getpass.getpass('ArchivesSpacew password: '))
print(s)
print('Success!')