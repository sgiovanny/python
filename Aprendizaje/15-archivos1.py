# abrimos el archivo e imprimimos el resultado 

def app():
    with open('archivo.txt') as archivo:  # por default se abre en modo lectura
        for contenido in archivo:
            print(contenido.rstrip())




app()