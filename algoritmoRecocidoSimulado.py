import math
import random

# Función de energía (puedes modificarla según tu problema)
def energia(solucion):
    # En este ejemplo, la energía es la suma de los cuadrados de los elementos de la solución
    return sum(x**2 for x in solucion)

# Función de vecino (puedes modificarla según tu problema)
def vecino(solucion, temperatura):
    # En este ejemplo, se realiza una pequeña perturbación en un valor aleatorio de la solución
    indice = random.randint(0, len(solucion)-1)
    nueva_solucion = solucion[:]
    nueva_solucion[indice] += random.uniform(-0.5, 0.5) * temperatura
    return nueva_solucion

# Algoritmo de recocido simulado
def recocido_simulado(solucion_inicial, temperatura_inicial, factor_enfriamiento, iteraciones_por_temperatura):
    solucion_actual = solucion_inicial
    temperatura_actual = temperatura_inicial
    
    while temperatura_actual > 0.01:  # Condición de parada
        for _ in range(iteraciones_por_temperatura):
            nueva_solucion = vecino(solucion_actual, temperatura_actual)
            delta_energia = energia(nueva_solucion) - energia(solucion_actual)
            if delta_energia < 0 or random.random() < math.exp(-delta_energia / temperatura_actual):
                solucion_actual = nueva_solucion
        temperatura_actual *= factor_enfriamiento
    
    return solucion_actual

# Parámetros
solucion_inicial = [random.uniform(-10, 10) for _ in range(5)]  # Solución inicial aleatoria
temperatura_inicial = 100.0
factor_enfriamiento = 0.95
iteraciones_por_temperatura = 100

# Ejecución del algoritmo
solucion_final = recocido_simulado(solucion_inicial, temperatura_inicial, factor_enfriamiento, iteraciones_por_temperatura)

print("Solución final:", solucion_final)
print("Energía de la solución final:", energia(solucion_final))
