# ackley.py
# Actividad: Optimización ciega
# Materia: Inteligencia Computacional
#
# Paquete Ackley, contiene la función Ackley.
#
# Autor: Santiago Díaz Guevara A01252554
# Fecha: 16-FEB-22

import math

def ackley(a, b, c, x):
    """
    Función Ackley
    https://www.sfu.ca/~ssurjano/ackley.html
    """

    d = len(x)

    return - a * math.exp(
        - b * math.sqrt(
            (1 / d) * sum(map(lambda xi : xi * xi, x))
        )
    ) - math.exp(
        (1 / d) * sum(map(lambda xi : math.cos(c * xi), x))
    ) + a + math.exp(1)
