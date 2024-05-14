# ################################ Maestría en Aplicaciones de Información Espacial ################################
# ################################ Introducción a las técnicas inteligentes de resolución de problemas de planificación, secuenciación y ejecución ################################
# ################################ Trabajo práctico Nº: 5 ################################
# ################################ Ejercicio 6: Crea un programa que simule una calculadora simple con funciones para suma, resta, multiplicación y división. ################################

# Pedir al usuario que ingrese el primer número
print("######Bienvenidos a la calculadora más sencilla del mundo######")
try:
    a = float(input("Por favor, introduzca el primer número: "))
except:
    ErrorValue = print("El símbolo ingresado debe ser un número. Vuelva a intentarlo.")
    exit(1)
    
# Pedir al usuario que ingrese el segundo número
try:
    b = float(input("Por favor, introduzca el primer número: "))
except:
    ErrorValue = print("El símbolo ingresado debe ser un número. Vuelva a intentarlo.")
    exit(1)

# Defino las funciones de la calculadora
def suma (a,b):
    resultado = a + b
    return resultado

def resta (a,b):
    resultado = a - b
    return resultado

def multiplicacion (a,b):
    resultado = a * b
    return resultado

def division (a,b):
    if b != 0:
        resultado = a / b
        return resultado
    else:
        return "Error: División por cero."

signo = {
    '+': suma,
    '-': resta,
    '*': multiplicacion,
    '/': division
}

# Verificar que el símbolo ingresado esté dentro de los permitidos
operacion = input("Por favor, introduzca la operación por su símbolo (+, -, *, /): ")

if operacion not in signo:
    print("El símbolo ingresado debe estar dentro de los permitidos (+, -, *, /). Vuelva a intentarlo.")
    exit(1)

# Calcular la operación
calculo = signo[operacion](a,b)

# Imprimir la asignación
print(f"El resultado final de operar mediante {operacion}, los valores {a} y {b}, es de {calculo}.")



# Modo de ejecución: Abrir en terminal python con "./eje6.py", dentro de la carpeta contenedora del archivo.