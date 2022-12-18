# La estructura básica del código es la siguiente:

- En la primera línea importamos tres librerías de Python para trabajar con números complejos (cmath), números reales (math) y también una librería para operar con números fraccionarios (fractions).

- Luego definimos la función solve_quadratic_equation (), que recibe como argumentos los coeficientes a, b y c de una ecuación cuadrática.

- Dentro de la función primero comprobamos si a es cero. Si es cero, se genera una excepción.

- Después calculamos el discriminante para la ecuación cuadrática.

- Si el discriminante es menor que cero, calculamos las soluciones para x1 y x2 usando cmath.sqrt ().

- Si el discriminante es igual a cero, calculamos la solución para x usando math.sqrt ().

- Si el discriminante es mayor que cero, calculamos las soluciones para x1 y x2 usando math.sqrt ().

- Por último, la función devuelve el resultado de x1 y x2.

- En la siguiente línea iniciamos el ciclo while para pedir los valores de los coeficientes a, b y c.

- Dentro del ciclo while pedimos los valores de los coeficientes a, b y c como una fracción usando Fraction ().

- Después, asignamos a una variable el valor de salida "return" de la función solve_quadratic_equation ().

- Por último, imprimimos las soluciones de acuerdo a los valores de los coeficientes a, b y c.
