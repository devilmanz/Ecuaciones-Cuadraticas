import cmath # para operar con numeros compejos
import math # para trabajar mejor con numeros reales
from fractions import Fraction # para operar con numeros fraccionarios

def solve_quadratic_equation(a, b, c):
  
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
        try: 
            a = Fraction(input("Valor de a: "))
            if a != 0:
                break
            print("El coeficiente a no puede ser cero, por favor introduce un valor distinto de cero.")
        except ValueError:
            print("Por favor introduce un número en lugar de letras.")

    try:
        b = Fraction(input("Valor de b: "))
        c = Fraction(input("Valor de c: "))
    except ValueError:
            print("Por favor introduce un número en lugar de letras.")
            continue #volvemos a pedir los valores

    #Asignamos a una variable el valor de salida "return" de la función incial
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
