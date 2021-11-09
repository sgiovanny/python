pregunta = 'Escribe un numero y te dire si es par o impar \r\n '
pregunta += ' (Escribe cerrar para cancelar la ejecuciion del programa)'

preguntar = True

while preguntar:
    # Mezclamos con operadores
    numero = input(pregunta)
    if numero == 'cerrar':
        preguntar = False
    else:
        numero = int(numero)
        if numero % 2 ==0:
            print(f'El número {numero} es Par')
        else:
            print(f'El número {numero} es Impar')


