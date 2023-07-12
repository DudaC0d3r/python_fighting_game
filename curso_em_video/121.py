import urllib
import urllib.request

try: 
    site1 = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.request.URLError:
    print('O Site não está acessível no momento')
else:
    print('Consegui abrir o site com sucesso!')