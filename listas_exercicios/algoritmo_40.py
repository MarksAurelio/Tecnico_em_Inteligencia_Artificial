""" Algoritmo 40 – Entrar com dois números inteiros e imprimir a seguinte saída: Dividendo Divisor Quociente Resto """

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

quociente = dividendo // divisor
resto = dividendo % divisor

print("\n--- Resultados ---")
print(f"Dividendo: {dividendo}")
print(f"Divisor: {divisor}")
print(f"Quociente: {quociente}")
print(f"Resto: {resto}")
