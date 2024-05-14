# ################################ Maestría en Aplicaciones de Información Espacial ################################
# ################################ Introducción a las técnicas inteligentes de resolución de problemas de planificación, secuenciación y ejecución ################################
# ################################ Trabajo práctico Nº: 5 ################################
# ################################ Ejercicio 2: Utilice la librería os para listar todos los directorios dentro del directorio “/dev”. ################################

import os

# Ruta del directorio que deseas explorar
directorio = 'C:\Windows\System32'

# Lista para almacenar los nombres de los directorios
directorios = []

# Recorre cada entrada en el directorio especificado
for entrada in os.listdir(directorio):
    # Construye la ruta completa de la entrada
    ruta_completa = os.path.join(directorio, entrada)
    # Comprueba si la entrada es un directorio
    if os.path.isdir(ruta_completa):
        directorios.append(entrada)

# Imprime los directorios encontrados
for d in directorios:
    print(d)


# Modo de ejecución: abrir en terminal python con "./eje2.py", dentro de la carpeta contenedora del archivo.