# ################################ Maestría en Aplicaciones de Información Espacial ################################
# ################################ Introducción a las técnicas inteligentes de resolución de problemas de planificación, secuenciación y ejecución ################################
# ################################ Trabajo práctico Nº: 5 ################################
# ################################ Ejercicio 4: Reemplace el ejercicio 3 por una implementación con parámetros pasados por consola usando la librería sys. ################################

import sys

sueldo = float(sys.argv[1])

# Verificar que el sueldo no sea cero ni negativo
if sueldo <= 0:
    print("El sueldo no puede ser 0 o negativo. Vuelva a intentarlo.")
    exit(1)

# Tomar el rango de los argumentos y verificar su validez
rango = sys.argv[2]
if rango not in ['1', '2', '3']:
    print("El rango debe ser 1, 2 o 3. Vuelva a intentarlo.")
    exit(1)

# Diccionario que emula la funcionalidad de 'switch'
factor_asignacion = {
    '1': 0.83,
    '2': 1.20,
    '3': 5
}

# Calcular la asignación usando el diccionario
asignacion = sueldo * factor_asignacion[rango]

# Imprimir la asignación
print(f"La asignación para el empleado con sueldo de {sueldo} y rango {rango} es de {asignacion}.")

# Modo de ejecución: abrir en terminal python con "./eje4.py" junto con los parámetros sueldo y rango (Por ejemplo, "./eje4.py 500 2"), dentro de la carpeta contenedora del archivo.