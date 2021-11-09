
# Definimos la clase 
class Restaurant:

    # Inicializamos el constructor 
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.__precio = precio 

    def mostrar_informacion(self):
        print(f'Nombre {self.nombre}, Categoria {self.categoria}, Precio {self.__precio}')


    # Getters y SEtters (Obtner y modificar los valores)
    def get_precio(self):
        return(self.__precio)
    
    def set_precio(self, precio):
        self.__precio = precio



# Instanciar la clase
restaurant = Restaurant('Piozza una','comida italiana',50)
restaurant.mostrar_informacion()
precio = restaurant.get_precio()
print(precio)

restaurant.set_precio(6698)
restaurant.get_precio()



