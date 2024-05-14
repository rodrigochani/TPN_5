# ################################ Maestría en Aplicaciones de Información Espacial ################################
# ################################ Introducción a las técnicas inteligentes de resolución de problemas de planificación, secuenciación y ejecución ################################
# ################################ Trabajo práctico Nº: 5 ################################
# ################################ Ejercicio 7: Cree un programa en Python que imprima la hora del sistema, estado de memoria RAM y almacenamiento disponible en la partición montada en “c/”. ################################

import datetime
import psutil

def obtener_hora_sistema():
    # Obtener la hora actual del sistema
    return datetime.datetime.now()

def obtener_estado_ram():
    # Obtener información de la memoria RAM
    memoria = psutil.virtual_memory()
    return f"Total: {memoria.total / (1024 ** 3):.2f} GB, Usada: {memoria.used / (1024 ** 3):.2f} GB, Disponible: {memoria.available / (1024 ** 3):.2f} GB"

def obtener_almacenamiento_disponible():
    # Obtener información del almacenamiento en la partición C:
    uso_disco = psutil.disk_usage('C:/')
    return f"Total: {uso_disco.total / (1024 ** 3):.2f} GB, Usado: {uso_disco.used / (1024 ** 3):.2f} GB, Libre: {uso_disco.free / (1024 ** 3):.2f} GB"

# Imprimir la hora del sistema
print("Hora del sistema:", obtener_hora_sistema())

# Imprimir el estado de la memoria RAM
print("Estado de la memoria RAM:", obtener_estado_ram())

# Imprimir el almacenamiento disponible
print("Almacenamiento en C:/:", obtener_almacenamiento_disponible())

# Modo de ejecución: Instalar psutil ("pip install psutil"). Abrir en terminal python con "./eje7.py", dentro de la carpeta contenedora del archivo.