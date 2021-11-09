cancion = {
'artista':'metallica', ## llave y valor
'cancion':'Enter Sandman',
'lanzamiento' :1992,
'likes' : 3000
}

# Acceder a los elementos del diccionario
print(cancion['artista'])
print(cancion['lanzamiento'])

# mezclar con un string
artista = cancion['artista']
print(f'estoy escuchando {artista}')

print(cancion)


# agregar nuevos valores
cancion['playlist'] = 'Heavy Metal'
print(cancion)

# Reemplazar valor existente
cancion['cancion'] = 'lanzamiento'
print(cancion)