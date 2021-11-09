nombre = input('Cual es tu nombre : \r\n')

print(f'Hola {nombre}')

 # Leer datos que sea numeros
edad = input('Cual es tu edad?: ')

 # convertir edad string a entero 
edad = int(edad)

if edad>= 18:
   print('Ya puedes votar')
else:
   print('Aun eres mnenor de edad: ')


# Mezclarlo con operadores
numero = input('Agrega un numero y te dire si es par o no \r\n')
numero = int(numero)

if numero % 2 ==0:
    print('El numero es par ')
else:
    print('El numero es impar')

