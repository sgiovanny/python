
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


# Creamos una clase hijo de restaurant
class Hotel(Restaurant):
    # Inicializamos el constructor y agregamos la referencia al padre
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre,categoria,precio)


hotel = Hotel('Hotel POO','5 estrellas',156)


hotel.mostrar_informacion()