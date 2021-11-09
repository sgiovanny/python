
# Definimos un arreglo 
meses = ["Enero","Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

# imprimimos el valor del arreglo
print(meses[2:7])

# mezclamos el arreglo con el mensjae de texto
print(f'Estoy esperando el mes de {meses[11]} que es mi cumpleaños')

# Imprimimos el contenido del arreglo
print(meses)


# Agregamos un valor al contenido del arreglo
meses.append('Mes no definido')
print(meses)

# Eliminar un valor del arreglo
del meses[5]
print(meses)

# Eliminar ultimo valor del arreglo
meses.pop()
print(meses)

# Eliminar un valor del arreglo mendiante el indice
meses.pop(6)
print(meses)

# Eliminar un valor del arreglo mendiante el valor
meses.remove('Mayo')
print(meses)


# Ordenamos el arreglo por su valor
meses.sort()
print(meses)

