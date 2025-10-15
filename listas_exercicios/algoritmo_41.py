""" Algoritmo 41 – Entrar com quatro números e imprimir a média ponderada , sabendo-se que os pesos são respectivamente: 1, 2, 3 e 4. """

pesos = [1, 2, 3, 4]
soma_produtos = 0
soma_pesos = 0

for i in range(4):
  numeros = float(input(f"Digite o {i+1}° número: "))
  peso = pesos[i]
  soma_produtos += numeros * peso
  soma_pesos += peso
  media_ponderada = soma_produtos / soma_pesos
  print(f"A média ponderada é: {media_ponderada:.2f}")
