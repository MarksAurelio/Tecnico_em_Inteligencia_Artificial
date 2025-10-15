""" Algoritmo 42 – Entrar com um ângulo em graus e imprimir: seno, co-seno, tangente, secante, co-secante e co-tangente deste ângulo. Use o módulo math. """

import math

angulo_graus = float(input("Digite o ângulo em graus: "))

angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

secante = 1 / cosseno
cossecante = 1 / seno
cotangente = 1 / tangente

print("\n--- Resultados ---")
print(f"Ângulo em Graus: {angulo_graus}")
print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")
print(f"Secante: {secante:.2f}")
print(f"Cossecante: {cossecante:.2f}")
print(f"Cotangente: {cotangente:.2f}")
