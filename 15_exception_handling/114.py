# **EXE_114**

# > Crie um código em Pytho que teste se o site **Pudim** está acessivel pelo computador usado.

import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com.br')
except:  # any error
    print('error')
else:
    print('estamos dentro')
    # print(site.read()) # para ler o codigo fonte do site
