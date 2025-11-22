numero = int(input("Digite um número: "))
while True:
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
    numero = int(input("Digite outro número (ou um número negativo para sair): "))
    if numero < 0:
        print("Encerrando o programa.")
        break
    