import os

print(os.getcwd()) #Muestra por pantalla el directorio en el que el script se encuentra

# os.chdir('/home/oscar/Proyectos') #Cambia el directorio de operacion del script 
# print(os.getcwd()) #Imprime por pantalla el nuevo directorio de operacion

# print(os.listdir()) #Imprime por pantalla un arreglo de string correspondiente a cada sub directorio dentro del directorio de operacion

# os.mkdir('Nuevo-directorio') #Crea un nuevo directorio
# os.makedirs('/Nuevo-directorio/nuevo-sub-directorio') #Crea todos los directorios y subdirectorios en el string

# os.rmdir('Nuevo-directorio') #borra un directorio con ese nombre
# os.removedirs('/Nuevo-directorio/nuevo-sub-directorio') #Borra el dubdirectorio

# os.rename('nuevo-directorio','viejo-directorio') #cambia el nombre de un directorio o archivo

# os.stat('nuevo-directorio') #entrega metadata asociado al directorio o archivo (tamaño, fecha de creación, etc)

# accede a todos los directorios, subdirectorios y archivos desde la ruta inicial
""" for dirpath, dirnames, filenames in os.walk('/home/oscar/Kauel/Proyectos/PuenteChacao/python/chacao_env/'):
    print(dirpath)
    print(dirnames)
    print(filenames) """

# print(os.environ) #Imprime todas las variables de entorno del sistema. Se puede buscar por el valor de una especifica
# print(os.environ.get('GIO_LAUNCHED_DESKTOP_FILE'))

print(os.path.join('/home/oscar', 'nuevo_archivo.txt')) #Genera una nueva dirección correctamente