import cmath
import math
from fractions import Fraction

def solve_quadratic_equation(a, b, c):
    """Resuelve la ecuación cuadrática de la forma ax^2 + bx + c = 0 y
    devuelve las soluciones reales o complejas según corresponda. Si la
    ecuación tiene una solución real, devuelve una tupla con un único
    elemento. Si la ecuación tiene dos soluciones reales, devuelve una
    tupla con dos elementos. Si la ecuación tiene dos soluciones
    complejas, devuelve una tupla con dos elementos."""
    
    #Comprobamos si a es cero
    if a == 0:
        raise ValueError("El coeficiente a no puede ser cero")
    
    #Calculamos el discriminante
    d = (b**2) - (4*a*c)
    
    #Calculamos las soluciones x1 y x2
    if d < 0:
        x1 = (-b + cmath.sqrt(d))/(2*a)
        x2 = (-b - cmath.sqrt(d))/(2*a)
    elif d == 0:
        x = (-b + math.sqrt(d))/(2*a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        return (x1, x2)
    
    return (x1, x2)

#Iniciamos el ciclo
while True:
    #Pedimos los valores de los coeficientes a, b y c
    while True:
        print("Introduce los valores de los coeficientes a, b y c de la ecuación cuadrática: ax^2 + bx + c = 0")
        a = Fraction(input("Valor de a: "))
        if a != 0:
            break
        print("El coeficiente a no puede ser cero, por favor introduce un valor distinto de cero.")
    b = Fraction(input("Valor de b: "))
    c = Fraction(input("Valor de c: "))

    #Resolvemos la ecuación cuadrática
    solutions = solve_quadratic_equation(a, b, c)
    
    #Imprimimos las soluciones
    if all(solution == 0 for solution in solutions):
        print("Esta ecuación no tiene solución real ni compleja")
    elif len(solutions) == 1:
        x = solutions[0]
        print("Esta ecuación tiene una solución real: {:.3f}".format(x))
    else:
        x1, x2 = solutions
        if isinstance(x1, complex):
            print("Esta ecuación tiene dos soluciones complejas: {:.2f} y {:.2f}".format(x1, x2))
        else:
            print("Esta ecuación tiene dos soluciones reales: {:.2f} y {:.2f}".format(x1, x2))
