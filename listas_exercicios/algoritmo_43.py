""" Algoritmo 43 – Entrar com um número e imprimir o logaritmo desse número na base 10. """

import math

numero = float(input("Digite um número positivo: "))
logaritmo = math.log10(numero)
print(f"O logaritmo de {numero} na base 10 é: {logaritmo}")
