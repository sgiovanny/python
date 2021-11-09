def app():
    # Crear el archivo
    archivo = open('archivo.txt','w') # abre el archivo, si no exist elo crear y le da atributo de escritura

    # Generar numeros en archivo
    for i in range(0,20):
        archivo.write('Esta es la linea .. ' + str(i) + "\r\n")

    # Cerramos el archivo 
    archivo.close()
app()
