""" Algoritmo 92- Construir um algoritmo que leia dois números e efetue a adição. Caso o valor somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8; Caso o valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5. """

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))  

soma = numero_1 + numero_2  

if soma > 20:
    resultado = soma + 8
    print("O resultado é:", resultado)        
else:
    resultado = soma - 5
    print("O resultado é:", resultado)  
