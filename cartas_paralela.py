import random
import time
from concurrent.futures import ThreadPoolExecutor # concurrent.futures para ordenar en paralelo

# Definición de los valores y palos
valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
palos = ['corazones', 'tréboles', 'picas', 'diamantes', 'comodín']

# Función para generar una carta
def generar_carta():
    valor = random.choice(valores)# valor aleatorio
    palo = random.choice(palos)# palo aleatorio
    return (valor, palo) #retornar una tupla 

# Función que asigna un orden numérico a los valores y palos
def clave_ordenacion(carta):
    valor, palo = carta
    valor_orden = valores.index(valor) # Convierte el valor en índice (0-12)
    # Mapeo de los palos (corazones < tréboles < picas < diamantes < comodín)
    palo_orden = palos.index(palo)# Convierte el palo en índice (0-4)
    return (palo_orden, valor_orden)#Por ejemplo, una carta de 'J' de 'corazones' sería convertida a (0, 9).

# Función que divide las cartas en partes y ordena en paralelo
def ordenar_paralelo(cartas):
    def ordena_parte(parte): #ORDENA UNA PARTE DE LA LISTA DE CARTAS CON SORTED
        return sorted(parte, key=clave_ordenacion)
    
    # Dividir las cartas en 8 partes para 8 hilos de ejecución
    partes = [cartas[i::8] for i in range(8)]
    
    with ThreadPoolExecutor(max_workers=8) as executor: #CREO UN POOL DE HILOS MAX 8
        resultados = list(executor.map(ordena_parte, partes)) #EXECUTOR.MAP aplica ORDENAR.PARTE en paraleca a cada parte de las 8
    #El resultado es una lista de 8 partes ordenadas de las cartas.
    
    # Combina las partes ordenadas
    cartas_ordenadas = [carta for parte in resultados for carta in parte]
    return sorted(cartas_ordenadas, key=clave_ordenacion)

# Generar el conjunto de 4 millones de cartas
cartas = [generar_carta() for _ in range(4000000)]

# Medir el tiempo para el ordenamiento paralelo
start_time = time.time()
cartas_ordenadas_paralelo = ordenar_paralelo(cartas)
end_time = time.time()

print(f"Tiempo de ejecución paralelo: {end_time - start_time} segundos")
