


texto = 'Manta vs. 9 de Octubre'
equipos = texto.split('vs.')
equipoL = ''
equipoV = ''

if equipos.count!=0:
    equipoL = str(equipos[0].strip())
    equipoV = str(equipos[1].strip())



print(equipoL)
print(equipoV)