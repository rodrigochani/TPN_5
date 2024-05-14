# ################################ Maestría en Aplicaciones de Información Espacial ################################
# ################################ Introducción a las técnicas inteligentes de resolución de problemas de planificación, secuenciación y ejecución ################################
# ################################ Trabajo práctico Nº: 5 ################################
# ################################ Ejercicio 5: Cree un programa en BASH, que invoque a tres programas en python, donde cada uno es un contador (con avance cada un segundo) hasta un número que se pase por entrada. Cada programa en python debe imprimir el contador segundo-a-segundo: a. Identifique el PID de cada proceso python; b. ¿Los procesos de ejecutan de manera secuencial?, ¿Cómo hacer para que corran todos a la vez?. ################################

import sys
import time

# Tomar el límite del contador desde los argumentos de la línea de comandos
limite = int(sys.argv[1])

# Función de contador
for i in range(1, limite + 1):
    print(f"{i}")
    time.sleep(1)  # Esperar un segundo antes de continuar



# Modo de ejecución: se ejecuta desde eje5.sh, dentro de la carpeta contenedora del archivo.