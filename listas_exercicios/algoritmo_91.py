""" Algoritmo 91 – Construir um algoritmo que leia dois valores numéricos inteiros e efetue a adição; caso o resultado seja maior que 10, apresentá-lo. """

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

soma = numero_1 + numero_2

if soma > 10:
    print("A soma é:", soma)        
else:
    print("A soma é menor ou igual a 10.")
