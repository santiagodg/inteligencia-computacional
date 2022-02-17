# busqueda.py
# Actividad: Optimización ciega
# Materia: Inteligencia Computacional
# 
# Algoritmos de búsqueda de 'un padre, varios hijos' y 'varios padres-varios
# hijos' con y sin traslape generacional.
#
# Autor: Santiago Díaz Guevara A01252554
# Fecha: 15 de febrero del 2022
#
# * Contiene una clase principal: `BlindOptimizer`.
# * Contiene un enumerador de estrategias para realizar la búsqueda
#   ciega: `BlindOptimizerAlgorithm`.
# * Contiene una estructura de parámetros para inicializar
#   `BlindOptimizer`: `BlindOptimizerParameters`.

import random

from enum import Enum

class BlindOptimizerAlgorithm(Enum):
    """
    Enumerador sobre las estrategias de búsqueda para optimización ciega.  
    """

    UN_PADRE_VARIOS_HIJOS_SIN_TRASLAPE_GENERACIONAL = 1
    UN_PADRE_VARIOS_HIJOS_CON_TRASLAPE_GENERACIONAL = 2
    VARIOS_PADRES_VARIOS_HIJOS_SIN_TRASLAPE_GENERACIONAL = 3
    VARIOS_PADRES_VARIOS_HIJOS_CON_TRASLAPE_GENERACIONAL = 4

class BlindOptimizerParameters:
    """
    Parámetros para inicializar el `BlindOptimizer`.
    """

    estrategia: BlindOptimizerAlgorithm = BlindOptimizerAlgorithm.UN_PADRE_VARIOS_HIJOS_SIN_TRASLAPE_GENERACIONAL
    """
    La estrategia de búsqueda. Debe ser un `BlindOptimizerAlgorithm`.
    """
 
    generar_al_azar = lambda: None
    """
    Función que no recibe nada y genera un nuevo 'padre' al azar cada vez que se le llama. 
    """

    
    criterio = lambda padre_anterior, padre_actual : True
    """
    Función que devuelve verdadero si se ha llegado a un final en la iteración sobre generaciones.
    Recibe una instancia del padre de la generación anterior y del padre de la generación actual,
    en ese orden. 
    """

    mutar = lambda padre : None
    """
    Función que toma un 'padre' y devuelve un 'hijo' tras aplicarle una mutación.
    """

    mejor = lambda hijos : None
    """
    Función que devuelve el mejor 'hijo' de una lista de 'hijos'.
    """

    seleccionar_mejores = lambda hijos : None
    """
    Función que devuelve una lista de los n mejores 'padres' de la lista ingresada.
    Recibe una lista de 'hijos', y la cantidad de 'padres' a regresar.
    
    Solo se usa en estrategias de varios padres.
    """

    num_hijos: int = 10
    """
    Número de hijos por generación.
    """

    num_padres: int = 5
    """
    Número de padres por generación
    
    Solo se usa en estrategias de varios padres.
    """

class Result:
    """
    Estructura que contiene el resultado de la ejecución de un 
    """
    
    def __init__(self, x, generations: int):
        """
        x: valores de solución para x
        generations: cantidad de generaciones que tardó en alcanzar la solución
        """
        self.x = x
        self.generations = generations


class BlindOptimizer:
    """
    Ejecuta algoritmos de búsqueda por medio de optimización ciega.

    `BlindOptimizer` es un ejecutor genérico. Cada vez que se vaya a usar,
    se deben ingresar las funciones que se requieren, especificadas en `BlindOptimizerParams`.
    """

    def __init__(self, params: BlindOptimizerParameters):
        """
        Inicializa un `BlindOptimizer`.
        """

        self.params = params

    def run(self) -> Result | str:
        """
        Ejecuta el optimizador de acuerdo a los parámetros ingresados y a la estrategia seleccionada.
        Devuelve un `Result` o un mensaje de error.
        """

        if self.params.estrategia == BlindOptimizerAlgorithm.UN_PADRE_VARIOS_HIJOS_SIN_TRASLAPE_GENERACIONAL:
            return self.__un_padre_varios_hijos_sin_traslape_generacional()
        elif self.params.estrategia == BlindOptimizerAlgorithm.UN_PADRE_VARIOS_HIJOS_CON_TRASLAPE_GENERACIONAL:
            return self.__un_padre_varios_hijos_con_traslape_generacional()
        elif self.params.estrategia == BlindOptimizerAlgorithm.VARIOS_PADRES_VARIOS_HIJOS_SIN_TRASLAPE_GENERACIONAL:
            return self.__varios_padres_varios_hijos_sin_traslape_generacional()
        elif self.params.estrategia == BlindOptimizerAlgorithm.VARIOS_PADRES_VARIOS_HIJOS_CON_TRASLAPE_GENERACIONAL:
            return self.__varios_padres_varios_hijos_con_traslape_generacional()
        
        return "Failed to match search strategy"

    def __un_padre_varios_hijos_sin_traslape_generacional(self) -> Result:
        """
        Devuelve el valor que cumple con el criterio especificado a través del
        método de búsqueda de 'un padre, varios hijos' sin traslape generacional.
        """

        padre_anterior = None
        padre_actual = self.params.generar_al_azar()

        generations = 0

        while not self.params.criterio(padre_anterior, padre_actual):
            hijos = []

            for _ in range(self.params.num_hijos):
                hijos.append(self.params.mutar(padre_actual))
            
            padre_anterior = padre_actual
            padre_actual = self.params.mejor(hijos)

            generations = generations + 1

        return Result(padre_actual, generations)

    def __un_padre_varios_hijos_con_traslape_generacional(self) -> Result:
        """
        Devuelve el valor que cumple con el criterio especificado a través del
        método de búsqueda de 'un padre, varios hijos' con traslape generacional.
        """

        padre_anterior = None
        padre_actual = self.params.generar_al_azar()

        generations = 0

        while not self.params.criterio(padre_anterior, padre_actual):
            hijos = []

            for _ in range(self.params.num_hijos):
                hijos.append(self.params.mutar(padre_actual))
            
            padre_anterior = padre_actual
            hijos.append(padre_actual)
            padre_actual = self.params.mejor(hijos)

            generations = generations + 1

        return Result(padre_actual, generations)

    def __varios_padres_varios_hijos_sin_traslape_generacional(self) -> Result:
        """
        Devuelve el valor que cumple con el criterio especificado a través del
        método de búsqueda de 'varios padres, varios hijos' sin traslape generacional.
        """

        mejor_padre_anterior = None
        padres_actuales = []
        
        for _ in range(self.params.num_padres):
            padres_actuales.append(self.params.generar_al_azar())

        generations = 0

        while not self.params.criterio(mejor_padre_anterior, self.params.mejor(padres_actuales)):
            hijos = []

            for _ in range(self.params.num_hijos):
                padre = random.choice(padres_actuales)
                hijos.append(self.params.mutar(padre))
            
            mejor_padre_anterior = self.params.mejor(padres_actuales)
            padres_actuales = self.params.seleccionar_mejores(hijos, self.params.num_padres)

            generations = generations + 1

        return Result(self.params.mejor(padres_actuales), generations)

    def __varios_padres_varios_hijos_con_traslape_generacional(self) -> Result:
        """
        Devuelve el valor que cumple con el criterio especificado a través del
        método de búsqueda de 'varios padres, varios hijos' con traslape generacional.
        """

        mejor_padre_anterior = None
        padres_actuales = []
        
        for _ in range(self.params.num_padres):
            padres_actuales.append(self.params.generar_al_azar())

        generations = 0

        while not self.params.criterio(mejor_padre_anterior, self.params.mejor(padres_actuales)):
            hijos = []

            for _ in range(self.params.num_hijos):
                padre = random.choice(padres_actuales)
                hijos.append(self.params.mutar(padre))
            
            mejor_padre_anterior = self.params.mejor(padres_actuales)
            hijos = hijos + padres_actuales
            padres_actuales = self.params.seleccionar_mejores(hijos, self.params.num_padres)

            generations = generations + 1

        return Result(self.params.mejor(padres_actuales), generations)
