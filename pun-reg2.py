import requests
import os
import random
import string
import json
import sys

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'https://swagbuckssl.xyz/api.php?act=register'

names = json.loads(open('names.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))
#in range = numero de caracteres de la password
	username = name.lower() + name_extra + '@gmail.com'
	password = ''.join(random.choice(chars) for i in range(12))
#El nombre del campo que se rellena xd
	requests.post(url, allow_redirects=False, data={
		'fullname': username,
		'username': username,
		'email': username,
		'password': password,
	})
    

	print ('Inyectando %s y password %s a la base de datos de %s') % (username, password, url)
