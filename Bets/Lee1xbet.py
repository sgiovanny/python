
import json
from  urllib import request


CARPETA = 'c:/SistemasGT/Proyectos/git/python/python/Bets/'
EXTENSION = '.json' # extension de archivos 



url = "https://1xbet.ec/LineFeed/Get1x2_VZip?sports=1&champs=276999&count=50&lng=es&tf=2200000&mode=4&country=209&getEmpty=true"

payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
  'Accept': '*/*',
  'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
  'X-Requested-With': 'XMLHttpRequest',
  'X-KL-Ajax-Request': 'Ajax_Request',
  'Connection': 'keep-alive',
  'Referer': 'https://1xbet.ec/es/line/Football/276999-Ecuador-Serie-A/',
  'Cookie': 'lng=es; flaglng=es; is_rtl=1; fast_coupon=true; v3tr=1; typeBetNames=full; auid=LYd5HWGG1uZHrX3IEB2xAg==; _ga=GA1.2.177373912.1636226800; _ym_uid=1636226801185778532; _ym_d=1636226801; sh.session_be98639c=51f2e394-9059-4a67-b892-b755e93d7281; pushfree_status=canceled; SESSION=c94132e04d0f7ee5f97609e64e8f846f; dnb=1; _glhf=1636423346; visit=1-8ccf84e4591cf33735342be73cde1c6e; coefview=0; ggru=146; completed_user_settings=true; _gid=GA1.2.1538118644.1636405500; _ym_isad=2; _ym_visorc=b',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'TE': 'trailers'
}

respuesta = request.urlopen(url)
contenido = respuesta.read()
json_obtenido = json.loads(contenido.decode('utf-8'))



# print(json_obtenido)
print('Leemos el Json de 1xBET - Para los partidos de Ecuador')
# print(json_obtenido)

print('Comenzamos a iterar el contenido de cada linea')
for item in json_obtenido['Value']:
    
    print('Liga\r\n')
    print('Partido ' + item['O1'] + '-' + item['O2'])

    print('========\r\n')
    print(item['L'])
   

    for a in item['E']:
        print('\r\n Linea 1')
        print(a)
