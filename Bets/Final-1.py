
import json
from  urllib import request


class Eventos:

    def __init__(self,id,descripcion,equipoL,equipoV,pais,liga):
        self.id = id
        self.descripcion = descripcion
        self.equipol = equipoL
        self.equipov = equipoV
        self.pais = pais
        self.liga = liga
    
    def add(self,id,descripcion,equipol,equipov,pais,liga):
            self.eventos[id] = id
            self.eventos[descripcion] = descripcion # Agrega el elemento al diccionario
            self.eventos[equipol] = equipol # Agrega el elemento al diccionario
            self.eventos[equipov] = equipov  # Agrega el elemento al diccionario
            self.eventos[pais] = pais # Agrega el elemento al diccionario
            self.eventos[liga] = liga  # Agrega el elemento al diccionario

            # print()

    def mostrar(self):
        print(self)
        print("----")
        #print("Id: {}, Descripcion: {}, Eq1: {}, Eq2: {}".format(id, descripcion,equipol,equipov))
        #print("Id: {}, Descripcion: {} {} {} ".format(id, descripcion, equipol, equipov ))




obj = []
obj.append(Eventos( '01','manta vs 9 de octubre','manta','9 de octubre','ecuador','liga ecuatoriana'))

for x1 in obj:
    print(x1.mostrar())





url = "https://sb1capi-altenar.biahosted.com/Sportsbook/GetEvents?timezoneOffset=300&langId=4&skinName=equabet&configId=1&culture=es-ES&deviceType=Desktop&numformat=en&sportids=0&categoryids=0&champids=1000000190&group=AllEvents&period=periodall&withLive=false&outrightsDisplay=none&marketTypeIds=&couponType=0&startDate=2021-11-06T20%3A52%3A00.000Z&endDate=2021-11-13T20%3A52%3A00.000Z"

payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
  'Accept': '*/*',
  'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
  'Origin': 'https://sb1client-altenar.biahosted.com',
  'Connection': 'keep-alive',
  'Referer': 'https://sb1client-altenar.biahosted.com/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site'
}

respuesta = request.urlopen(url)
contenido = respuesta.read()
json_obtenido = json.loads(contenido.decode('utf-8'))


# print(json_obtenido)
print('Leemos el Json de Ecuabet - Para los partidos de Ecuador')
print(json_obtenido)

print('Comenzamos a iterar el contenido de cada linea')
for item in json_obtenido['Result']['Items']:
  # print(item)

  for x in item['Events']:
    texto = str(x['Name']).strip()
    equipos = texto.split('vs.')
    equipoL = ''
    equipoV = ''
    pais = x['CategoryName']
    liga = x['ChampName']


    if equipos.count!=0:
      equipoL = str(equipos[0].strip())
      equipoV = str(equipos[1].strip())




    #print(x['Name'])
    print(f'\r\n {x}')




    #for p in x['Items']:
    #  print(p)
    #  print('\r\n')

