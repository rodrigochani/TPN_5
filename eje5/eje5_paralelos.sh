# ################################ Maestría en Aplicaciones de Información Espacial ################################
# ################################ Introducción a las técnicas inteligentes de resolución de problemas de planificación, secuenciación y ejecución ################################
# ################################ Trabajo práctico Nº: 5 ################################
# ################################ Ejercicio 5: Cree un programa en BASH, que invoque a tres programas en python, donde cada uno es un contador (con avance cada un segundo) hasta un número que se pase por entrada. Cada programa en python debe imprimir el contador segundo-a-segundo: a. Identifique el PID de cada proceso python; b. ¿Los procesos de ejecutan de manera secuencial?, ¿Cómo hacer para que corran todos a la vez?. ################################

echo "Ingrese el número hasta el cual contarán los contadores:"
read limite

# Path del ejecutable de Python
python_path="/c/Users/rodri/AppData/Local/Programs/Python/Python312/python.exe"

# Ejecutar cada script de Python en background y capturar sus PIDs
echo "##### Los contadores se ejecutrán paralelamente #####"
$python_path eje5a.py $limite & PID1=$!
echo "Contador a ejecutándose con PID: $PID1"

$python_path eje5b.py $limite & PID2=$!
echo "Contador b ejecutándose con PID: $PID2"

$python_path eje5c.py $limite & PID3=$!
echo "Contador c ejecutándose con PID: $PID3"

# Esperar a que todos los procesos terminen
wait $PID1 $PID2 $PID3
echo "Todos los contadores han terminado."

# Modo de ejecución: Abrir en terminal Linux con "./eje5_secuencial.sh", dentro de la carpeta contenedora del archivo.