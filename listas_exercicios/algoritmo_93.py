""" Algoritmo 93 - Entrar com um número e imprimir a raiz quadrada do número caso ele seja positivo e o quadrado do número caso ele seja negativo. """

import math

numero = float(input("Digite um número: "))
if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print("A raiz quadrada de", numero, "é:", raiz_quadrada)
else:
    quadrado = numero ** 2
    print("O quadrado de", numero, "é:", quadrado)  
