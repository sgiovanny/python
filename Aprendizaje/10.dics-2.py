# Iniciar un diccionar vacio
jugador = {}

print(jugador)

#se une un jugador
jugador['nombre'] = 'Juan'
jugador['Puntaje'] = 0

print(jugador)

jugador['Puntaje'] = 100
print(jugador)

# evaluamos si existe el valor en el diccionario
print(jugador.get('consola', 'no existe ese valor en el diccionario'))


for llave, valor in jugador.items():
    print(llave)
    print(valor)


# Eliminamos valores del diccionario
del(jugador['nombre'])
del(jugador['Puntaje'])
print(jugador)
