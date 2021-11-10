# from _typeshed import Self


class PC():

    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3

    def __repr__(self):
        return str(self.__dict__)

    
    def carga_clase(self, lista):
        valores  = lista.split(',')

        if valores.count!=0:
            self.attr1 = str(valores[0].strip())
            self.attr2 = str(valores[1].strip()) 
            self.attr3 = str(valores[2].strip()) 

arr = []
arr.append(PC('a', 'b', 'c'))
arr.append(PC('d', 'e', 'f'))
arr.append(PC('g', 'h', 'i'))
arr.append(PC('j', 'k', 'l'))
print(arr)

for a in arr:
    print(a)

    
    x = PC
    x.carga_clase(a)
    print(x.descripcion)

    
