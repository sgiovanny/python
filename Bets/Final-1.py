
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
    
    def __repr__(self):
        return str(self.__dict__)        
    
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
obj.append(Eventos( '02','Bsc vs Olmedo','BSC','Olmedo','ecuador','liga ecuatoriana'))

print(repr(obj))

for x0 in obj:
    print(x0)




#for x1 in obj:
#    print(x1)
#    print(x1[0])


 