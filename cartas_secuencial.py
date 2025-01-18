import random
import time

# Definición de los valores y palos 
valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
palos = ['corazones', 'tréboles', 'picas', 'diamantes', 'comodín']

# Función para generar una carta ALEATORIA
def generar_carta():
    valor = random.choice(valores) # valor aleatorio
    palo = random.choice(palos) # palo aleatorio
    return (valor, palo)

# Función que asigna un orden numérico a cada carta (valor y palo)
def clave_ordenacion(carta):
    valor, palo = carta
    # Mapeo de los valores (2<3<4....<K<A)
    valor_orden = valores.index(valor)
    # Mapeo de los palos (corazones < tréboles < picas < diamantes < comodín)
    palo_orden = palos.index(palo)
    return (palo_orden, valor_orden) #Por ejemplo, una carta de 'J' de 'corazones' sería convertida a (0, 9).

# Función secuencial para ordenar las cartas
def ordenar_secuencial(cartas):
    return sorted(cartas, key=clave_ordenacion) #sorted() toma la lista de cartas y las ordena según la clave de SORTED

#La lista resultante estará ordenada primero por palo (de corazones a comodín) y, dentro de cada palo, por el valor de las cartas (de '2' a 'A').

# Generamos el conjunto de 4 millones de cartas
cartas = [generar_carta() for _ in range(4000000)]

# Medimos el tiempo para el ordenamiento secuencial

start_time = time.time()# registramos el tiempo justo antes de iniciar el proceso de ordenación.
cartas_ordenadas_secuencial = ordenar_secuencial(cartas)#ejecutamos la función de ordenación secuencial sobre el conjunto de cartas.
end_time = time.time() # registra el tiempo justo después de que se haya completado el proceso de ordenación.

print(f"Tiempo de ejecución secuencial: {end_time - start_time} segundos")
