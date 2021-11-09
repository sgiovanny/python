
# Definimos la clase 
class Restaurant:

    # Inicializamos el constructor 
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio 

    def mostrar_informacion(self):
        print(f'Nombre {self.nombre}, Categoria {self.categoria}, Precio {self.precio}')


    # Getters y SEtters (Obtner y modificar los valores)
    def get_precio(self):
        return(self.precio)
    
    def set_precio(self, precio):
        self.precio = precio


# Creamos una clase hijo de restaurant
class Hotel(Restaurant):
    # Inicializamos el constructor y agregamos la referencia al padre
    def __init__(self, nombre, categoria, precio,alberca):
        
        # Heredamos del padre
        super().__init__(nombre,categoria,precio)
        self.alberca = alberca
    

    # Re escribimos el metodo (polimorfismo)
    def mostrar_informacion(self):
        print(f'Nombre {self.nombre}, Categoria {self.categoria}, Precio {self.precio}, Alberca : {self.alberca}')    
    
    # Agregamos un metodo que solo existe en la clase hijo (Hotel)
    def get_alberca(self):
        return self.alberca


hotel = Hotel('Hotel POO','5 estrellas',156,'si')
hotel.mostrar_informacion()
alberca = hotel.get_alberca()
print(alberca)