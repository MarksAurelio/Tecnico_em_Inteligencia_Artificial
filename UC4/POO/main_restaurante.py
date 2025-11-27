from restaurante import Restaurante

print("Make Resturante")
print("1. Cadastrar Restaurante")
print("2. Listar Restaurante")
print("3. Ativar Restaurante")
print("4. Sair Restaurante")

opcao = input("Escolha uma opção: ")

p1 = Restaurante(nome="Enzo", tipo_de_cozinha="Industrial", avaliacao=10, preco_medio=10.00)

print(f"O nome do personagem é {p1.nome}")
print(f"O tipo de cozinha é {p1.tipo_de_cozinha}")
print(f"A avaliação é {p1.avaliacao}")
print(f"O preço médio é {p1.preco_medio}")

print("Restaurante criado com sucesso!")
