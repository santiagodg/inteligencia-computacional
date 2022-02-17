# main.py
# Actividad: Optimización ciega
# Materia: Inteligencia Computacional
#
# Este archivo contiene la ejecución de los algoritmos de búsqueda por medio de
# optimiazación ciega aplicados a la función de Ackley.
#
# Autor: Santiago Díaz Guevara A01252554
# Fecha: 16-FEB-22
#
# El ejercicio se separa en tres partes:
# - Algoritmos genéricos de búsqueda (busqueda.py)
# - Función Ackley (ackley.py)
# - Ejecución algoritmo de búsqueda aplicado sobre Ackley (main.py)

import busqueda
import ackley

import random
import math

#########################################################
#####       Constantes de instancia de Ackley     #######
#########################################################

ACKLEY_LOWER_BOUND = -32.768
ACKLEY_UPPER_BOUND = 32.768
ACKLEY_A = 20
ACKLEY_B = 0.2
ACKLEY_C = 2 * math.pi

#########################################################
###########      Constantes del Ejercicio     ###########
#########################################################

NUM_HIJOS: int = 20
NUM_PADRES: int = 5
PLUS_MINUS_VALUE: float = 5.0

STOPPING_DIFFERENCE: float = 0.05
"""
If difference between current parent and last parent is less than
`STOPPING_DIFFERENCE`, then stop. Improvement will be minimal after this and a
stopping point is needed to finish.
"""

#########################################################
########     Funciones Helper del Ejercicio     #########
#########################################################

def generar_al_azar():
    """
    Devuelve una tupla de dos valores que son random entre ACKLEY_LOWER_BOUND y
    ACKLEY_UPPER_BOUND.
    """
    
    return (random.uniform(ACKLEY_LOWER_BOUND, ACKLEY_UPPER_BOUND), random.uniform(ACKLEY_LOWER_BOUND, ACKLEY_UPPER_BOUND))

def criterio(padre_anterior, padre_actual):
    """
    Devuelve verdadero si el valor de ackley del padre actual es menor al del
    padre anterior y la diferencia es muy pequeña.
    """

    if padre_anterior == None:
        return False

    ackley_anterior = ackley.ackley(ACKLEY_A, ACKLEY_B, ACKLEY_C, padre_anterior)
    ackley_actual = ackley.ackley(ACKLEY_A, ACKLEY_B, ACKLEY_C, padre_actual)

    return ackley_anterior > ackley_actual and abs(ackley_anterior - ackley_actual) < STOPPING_DIFFERENCE

def mutar(padre):
    """
    Devuelve un valor cercano a `padre`. Cada valor de la tupla es sumado a un
    valor aleatorio entre +/- PLUS_MINUS_VALUE.
    """

    mutated = (padre[0] + random.uniform(-PLUS_MINUS_VALUE, PLUS_MINUS_VALUE), padre[1] + random.uniform(-PLUS_MINUS_VALUE, PLUS_MINUS_VALUE))
    clamped = (max(min(mutated[0], ACKLEY_UPPER_BOUND), ACKLEY_LOWER_BOUND), max(min(mutated[1], ACKLEY_UPPER_BOUND), ACKLEY_LOWER_BOUND))

    return clamped

def mejor(hijos):
    """
    Devuelve el valor más óptimo del arreglo especificado.
    """

    curr_min = float('inf')
    min_index = -1
    for i, v in enumerate(map(lambda x : ackley.ackley(ACKLEY_A, ACKLEY_B, ACKLEY_C, x), hijos)):
        if curr_min > v:
            curr_min = v
            min_index = i

    return hijos[min_index]

def seleccionar_mejores(hijos, m):
    """
    Devuelve los `m` mejores valores del arreglo especificado.
    """
    
    hijos.sort(reverse=False, key=lambda hi : ackley.ackley(ACKLEY_A, ACKLEY_B, ACKLEY_C, hi))
    res = hijos[:m]
    return res


def main():
    """
    Ejecuta el programa
    """

    # Estructurar los parámetros para ejecutar el optimizador ciego.
    params = busqueda.BlindOptimizerParameters()
    params.generar_al_azar = generar_al_azar
    params.criterio = criterio
    params.mutar = mutar
    params.mejor = mejor
    params.seleccionar_mejores = seleccionar_mejores
    params.num_hijos = 10
    params.num_padres = 5

    # Inicializar optimizador ciego
    optimizer = busqueda.BlindOptimizer(params)

    # Correr optimizador con estrategia
    # UN_PADRE_VARIOS_HIJOS_SIN_TRASLAPE_GENERACIONAL
    print("Running BlindOptimizer with:")
    print("    Strategy: Un padre, varios hijos sin traslape generacional")
    print("    Hijos por generación:", params.num_hijos)
    params.estrategia = busqueda.BlindOptimizerAlgorithm.UN_PADRE_VARIOS_HIJOS_SIN_TRASLAPE_GENERACIONAL
    resultado_1 = optimizer.run()
    print("    Resultado:", resultado_1.x, "en", resultado_1.generations, "generaciones")
    print()

    # Correr optimizador con estrategia
    # UN_PADRE_VARIOS_HIJOS_CON_TRASLAPE_GENERACIONAL
    print("Running BlindOptimizer with:")
    print("    Strategy: Un padre, varios hijos con traslape generacional")
    print("    Hijos por generación:", params.num_hijos)
    params.estrategia = busqueda.BlindOptimizerAlgorithm.UN_PADRE_VARIOS_HIJOS_CON_TRASLAPE_GENERACIONAL
    resultado_2 = optimizer.run()
    print("    Resultado:", resultado_2.x, "en", resultado_2.generations, "generaciones")
    print()

    # Correr optimizador con estrategia
    # VARIOS_PADRES_VARIOS_HIJOS_SIN_TRASLAPE_GENERACIONAL
    print("Running BlindOptimizer with:")
    print("    Strategy: Varios padres, varios hijos sin traslape generacional")
    print("    Padres por generación:", params.num_padres)
    print("    Hijos por generación: ", params.num_hijos)
    params.estrategia = busqueda.BlindOptimizerAlgorithm.VARIOS_PADRES_VARIOS_HIJOS_SIN_TRASLAPE_GENERACIONAL
    resultado_3 = optimizer.run()
    print("    Resultado:", resultado_3.x, "en", resultado_3.generations, "generaciones")
    print()

    # Correr optimizador con estrategia
    # VARIOS_PADRES_VARIOS_HIJOS_CON_TRASLAPE_GENERACIONAL
    print("Running BlindOptimizer with:")
    print("    Strategy: Varios padres, varios hijos sin traslape generacional")
    print("    Padres por generación:", params.num_padres)
    print("    Hijos por generación: ", params.num_hijos)
    params.estrategia = busqueda.BlindOptimizerAlgorithm.VARIOS_PADRES_VARIOS_HIJOS_CON_TRASLAPE_GENERACIONAL
    resultado_4 = optimizer.run()
    print("    Resultado:", resultado_4.x, "en", resultado_4.generations, "generaciones")
    print()

if __name__ == "__main__":
    main()
