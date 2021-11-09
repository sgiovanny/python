from genericpath import exists
import os  # Funcion para manejar archivos

CARPETA = 'c:/SistemasGT/Proyectos/git/python/python/Aprendizaje/contactos/'
EXTENSION = '.txt' # extension de archivos 


# Contactos Clase
class Contacto:
        def __init__(self, nombre, telefono, categoria):
            self.nombre = nombre
            self.telefono = telefono
            self.categoria = categoria
            
def app():

    # Verificamosy creamos la carpeta
    crear_directorios()

    # Mostramos el menu
    mostrar_menu()

    # Preguntar al usuario la opcion que desea realizar 
    preguntar = True

    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        #Ejecutar las opciones
        if opcion == 1:
            agregar_contactos()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        elif opcion == 6:
            print('\r\n Gracias por utilizar este programa \r\n')
            preguntar = False     
        else:
            print('Opcion no existente, intente de nuevo')

# muestra el menu opciones
def mostrar_menu():    
    print('Seleccione del Menú lo que desea hacer:')
    print('1) Agregar nuevo contacto')
    print('2) Editar Contacto ')
    print('3) Ver Contactos ')
    print('4) Buscar  Contacto')
    print('5) Eliminar Contacto')
    print('6) Salida del menu')


def crear_directorios():
    if not os.path.exists(CARPETA):
        # Creamos la carpeta 
        os.makedirs(CARPETA)




# Estamos creando la funcion de agregar contactos
def agregar_contactos():
    print('Escribe los datos para agregar el contacto')
    nombre_contacto = input('Nombre del contacto: \r\n')

    # validamos si existe el archivo
    existe = existe_contacto(nombre_contacto)
    
    if not existe:

        with open(CARPETA+nombre_contacto+ EXTENSION,'w') as archivo:

            telefono_contacto = input('Teléfono del contacto: \r\n')
            categoria_contacto = input('Categoria del contacto: \r\n')

            # instanciamos la calse
            contacto = Contacto(nombre_contacto,telefono_contacto,categoria_contacto)



            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('telefono: ' + contacto.telefono + '\r\n')
            archivo.write('categoria: ' + contacto.categoria + '\r\n')

            # mostramos n mensaje de exito
            print('\r\n Contacto creado correctamente \r\n')
    else:
        print('Ya existe el archivo ')

    # reiniciar la app
    app()

def editar_contacto():
    print('Escribe el contacto a editar')
    nombre_contacto = input('Nombre del contacto: \r\n')
    nombre_anterior = nombre_contacto
    existe = existe_contacto(nombre_contacto)
    if existe:
        with open(CARPETA+nombre_anterior+ EXTENSION,'w') as archivo:
            

            nombre_contacto = input('Agrega nuevo nombre: \r\n')
            telefono_contacto = input('Agrega el nuevo telefono: \r\n')
            categoria_contacto = input('Agrega la nueva Categoria: \r\n')            

            # instanciar
            contacto = Contacto(nombre_contacto,telefono_contacto,categoria_contacto)

            # Escribir en el archivo 
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('telefono: ' + contacto.telefono + '\r\n')
            archivo.write('categoria: ' + contacto.categoria + '\r\n')

        # Renombramos el archivo
        os.rename(CARPETA+nombre_anterior+ EXTENSION, CARPETA+nombre_contacto+ EXTENSION)

        # mostramos n mensaje de exito
        print('\r\n Contacto actualizado 2correctamente \r\n')


    else:
        print('no existe contacto, imposible editar ')

    # Reiniciar la aplicacion 
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo ) as contacto:
            for linea in contacto:
                #imprime los contenidos
                print(linea.rstrip())
    	    
            # imprime una linea 
            print('\r\n')

def buscar_contacto():
    nombre = input('seleccione el contacto que desea buscar \r\n')

    try:
        with open(CARPETA+nombre+EXTENSION) as contacto:
            print('\r\n Informacion del ctontacto: \r\n')
            for linea in contacto:
                print(linea.strip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)

def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea eliminar: \r\n ')

    try:
        os.remove(CARPETA+nombre+EXTENSION)
        print('Eliminado correctamente')
    except expression as identifier:
        print('No existe ese contacto ')
    
    #reiniciar la app
    app()



# Funcion que devuelve un valor 
def existe_contacto(nombre):
    return os.path.isfile(CARPETA+nombre+ EXTENSION)


app()


