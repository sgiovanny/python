class Restaurant:


    def agregar_restaurant(self, nombre):
        self.nombre = nombre # Atributo 

    def mostrar_informacion(self):
        print(f'Nombre {self.nombre}')



# Instanciar la clase
restaurant = Restaurant()

print(restaurant)

restaurant.agregar_restaurant('Pizeeria Dominos')
restaurant.mostrar_informacion()

# Segunda instancia
restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Otro Restaurant')
restaurant2.mostrar_informacion()

# mostrar a info de los dos

print(f'Info {restaurant.nombre}')
print(f'Info {restaurant2.nombre}')