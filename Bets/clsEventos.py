
class Eventos:

    def __init__(self,id,descripcion,equipoL,equipoV,pais,liga):
        self.id = id
        self.descripcion = descripcion
        self.equipol = equipoL
        self.equipov = equipoV
        self.pais = pais
        self.liga = liga
    

    def mostrar_eventos(self):
        texto = self.id + ' ' + self.descripcion + self.equipol + ' ' + self.equipov + ' ' + self.pais + ' ' + self.liga
        print(texto)     
    

