# from personagem import Personagem

# print('Hello World!')
# print("Make Pizza")
# print("1. Cadastrar Pizzaria")
# print("2. Listar Pizzaria")
# print("3. Ativar Pizzaria")
# print("4. Sair Pizzaria")

# opcao = int(input("Escolha uma opção: "))

# p1 = Personagem(nome="Enzo",
#                 idade=17,
#                 altura=1.75,
#                 peso=75,
#                 cor="pardo")

# print(f"O nome do personagem é {p1.nome}")
# print(f"A idade do personagem é {p1.idade}")
# print(f"O peso do personagem é {p1.peso}")
# print(f"A altura do personagem é {p1.altura}")
# print(f"A cor do personagem é {p1.cor}")
# print("Personagem criado com sucesso!")

from restaurante import Restaurante

print("Make Resturante")
print("1. Cadastrar Restaurante")
print("2. Listar Restaurante")
print("3. Ativar Restaurante")
print("4. Sair Restaurante")

opcao = int(input("Escolha uma opção: "))

p1 = Restaurante(nome="Enzo", tipo_de_cozinha="Industrial", avaliacao=10, preco_medio=10.00)

print(f"O nome do personagem é {p1.nome}")
print(f"O tipo de cozinha é {p1.tipo_de_cozinha}")
print(f"A avaliação é {p1.avaliacao}")
print(f"O preço médio é {p1.preco_medio}")

print("Restaurante criado com sucesso!")