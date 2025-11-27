from personagem import Personagem

print('Hello World!')
print("Make Pizza")
print("1. Cadastrar Pizzaria")
print("2. Listar Pizzaria")
print("3. Ativar Pizzaria")
print("4. Sair Pizzaria")

opcao = int(input("Escolha uma opção: "))

p1 = Personagem(nome="Enzo",
                idade=17,
                altura=1.75,
                peso=75,
                cor="pardo")

print(f"O nome do personagem é {p1.nome}")
print(f"A idade do personagem é {p1.idade}")
print(f"O peso do personagem é {p1.peso}")
print(f"A altura do personagem é {p1.altura}")
print(f"A cor do personagem é {p1.cor}")
print("Personagem criado com sucesso!")
