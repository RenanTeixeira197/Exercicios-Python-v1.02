# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("O site Pudim não está acessível.")
else:
    print("Consegui acessar o site pudim.com.br")
    print(site.read())
