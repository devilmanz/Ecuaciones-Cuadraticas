#Importamos la función sqrt para calcular la raíz cuadrada
from math import sqrt

#Iniciamos el ciclo
while True:
    #Pedimos los valores de los coeficientes a, b y c
    print("Introduce los valores de los coeficientes a, b y c de la ecuación cuadrática: ax2 + bx + c = 0")
    a = float(input("Valor de a: "))
    b = float(input("Valor de b: "))
    c = float(input("Valor de c: "))

    #Calculamos el discriminante
    d = (b**2) - (4*a*c)

    #Comprobamos si tiene solución
    if d < 0:
        print("Esta ecuación no tiene solución real")
    elif d == 0:
        x = (-b + sqrt(d))/(2*a)
        print("Esta ecuación tiene una solución real: ", x)
    else:
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b - sqrt(d))/(2*a)
        print("Esta ecuación tiene dos soluciones reales: ", x1, "y", x2)
        
    #Pedimos al usuario si quiere continuar
    continuar = input("¿Quieres continuar? (s/n): ")
    if continuar != "s":
        break
