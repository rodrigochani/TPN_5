# ################################ Maestría en Aplicaciones de Información Espacial ################################
# ################################ Introducción a las técnicas inteligentes de resolución de problemas de planificación, secuenciación y ejecución ################################
# ################################ Trabajo práctico Nº: 5 ################################
# ################################ Ejercicio 3: Haga un programa en python donde tome dos valores de entrada: sueldo y rango. Con ello, calcule la asignación que percibirá el empleado, considerando la tabla dada. ################################

# Pedir al usuario que ingrese el sueldo
sueldo = input("Por favor, introduce el sueldo del empleado: ")

# Verificar que el sueldo no sea cero ni negativo antes de proceder
if sueldo <= 0:
    print("El sueldo no puede ser 0 o negativo. Vuelva a intentarlo.")
    exit(1)

# Pedir al usuario que ingrese el rango
rango = input("Introduce el rango (1, 2, o 3): ")

# Verificar que el rango sea uno de los valores permitidos
if rango not in ['1', '2', '3']:
    print("El rango no puede ser distinto a 1, 2 o 3. Vuelva a intentarlo.")
    exit(1)

# Calcular la asignación basándose en el rango
if rango == '1':
    asignacion = sueldo * 0.83
elif rango == '2':
    asignacion = sueldo * 1.2
elif rango == '3':
    asignacion = sueldo * 5
     
# Imprimir la asignación
print(f"La asignación para el empleado con sueldo de {sueldo} y rango {rango} es de {asignacion}.")

# Modo de ejecución: abrir en terminal python con "./eje3.py", dentro de la carpeta contenedora del archivo.