# Optimización Ciega

## Objetivo de la actividad

Conocer el funcionamiento de los algoritmos más sencillos de optimización ciega.

## Instrucciones de la actividad

1. Instala Python3 o utiliza un notebook en la nube.
2. Programa los algoritmos de búsqueda de un padre-varios hijos y varios padres-varios hijos con y sin traslape generacional.
3. Leer sobre la Función [Ackley](https://www.sfu.ca/~ssurjano/ackley.html).
4. Utiliza los algoritmos programados para encontrar los valores de x que regresan el menor valor de la función Ackley en el intervalo LaTeX: -32.768 <= x_i <= 32.768. La variable x tiene 2 dimensiones (x_1 y x_2). 
5. Usar a=20, b=0.2 y c=2*pi.

Tips:

* Pueden usar funciones como np.argmin (Enlaces a un sitio externo.), np.argsort (Enlaces a un sitio externo.), np.concatenate (Enlaces a un sitio externo.) y slicing de arreglos (Enlaces a un sitio externo.) para evitarse algunos fors al momento de generar los hijos o sustituir a los padres con los hijos. Es una sugerencia, pueden hacerlo con fors.

* La curva de mejor encontrado puede tener al comienzo una desviación estándar pequeña debido a que la zona exterior del cono tiene una evaluación similar. La desviación estándar va a aumentar porque algunas soluciones de los experimentos van a lograr llegar al cono. Después de muchas iteraciones la desviación estándar va a empezar a disminuir porque más soluciones están logrando llegar al cono.
