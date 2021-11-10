class MisDeportes(object):

    def __init__(self, listado_deportes=None):
        if listado_deportes is None:
            self.listado_deportes = []
        else:
            self.listado_deportes = listado_deportes

    def add_deporte(self, deporte: str):
        self.listado_deportes.append(deporte)

    def __str__(self) -> str:
        str_con_el_resultado = 'Objeto de deportes: '
        for deporte in self.listado_deportes:
            str_con_el_resultado += "\n  * {}".format(deporte)
        return str_con_el_resultado

    def __repr__(self) -> str:
        representacion_interpretable = '{self.__class__.__name__}({self.listado_deportes})'.format(self=self)
        return representacion_interpretable


if __name__ == "__main__":
    mis_deportes = MisDeportes()

    mis_deportes.add_deporte('Running')
    mis_deportes.add_deporte('Futbol')
    mis_deportes.add_deporte('Ciclismo')

print(mis_deportes)


representacion_para_humanos1 =str(mis_deportes)
representacion_para_humanos2 = repr(mis_deportes)

print(representacion_para_humanos1)
print(representacion_para_humanos2)



