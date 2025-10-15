# Entrar com 8 números e, para cada número, imprimir o logaritmo desse número na base 10

import math

for i in range(8):
    try:
        num = float(input("Digite um número: "))
        if num > 0:
            logaritmo = math.log10(num)
            print(f"O logaritmo de {num} na base 10 é {logaritmo}")
        else:
            print("Número inválido. Digite um número positivo.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
