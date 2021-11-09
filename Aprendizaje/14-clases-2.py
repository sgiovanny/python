
# Definimos la clase 
class Restaurant:

    # Inicializamos el constructor 
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria # Default public el acceso 
        self.precio = precio

    def mostrar_informacion(self):
        print(f'Nombre {self.nombre}, Categoria {self.categoria}, Precio {self.precio}')



# Instanciar la clase
restaurant = Restaurant('Piozza una','comida italiana',50)
restaurant.mostrar_informacion()

restaurant2 = Restaurant('Piozza 2', 'comida chatarra', 36)
restaurant2.mostrar_informacion()

