from mercado_produto import Mercado_Produto

lista_produtos = [
    Mercado_Produto("Arroz", 20.0, 50, "2024-12-31"),
    Mercado_Produto("Feijão", 8.0, 100, "2024-11-30"),
    Mercado_Produto("Macarrão", 5.0, 200, "2025-01-15"),
]
def menu():
    while True:
        print("Menu de Produtos:")
        print("1. Listar Produtos")
        print("2. Atualizar Preço")
        print("3. Atualizar Quantidade")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            for produto in lista_produtos:
                print(produto)
        elif escolha == '2':
            nome_produto = input("Digite o nome do produto para atualizar o preço: ")
            novo_preco = float(input("Digite o novo preço: "))
            for produto in lista_produtos:
                if produto.nome == nome_produto:
                    produto.atualizar_preco(novo_preco)
                    print("Preço atualizado com sucesso!")
                    break
            else:
                print("Produto não encontrado.")
        elif escolha == '3':
            nome_produto = input("Digite o nome do produto para atualizar a quantidade: ")
            nova_quantidade = int(input("Digite a nova quantidade: "))
            for produto in lista_produtos:
                if produto.nome == nome_produto:
                    produto.atualizar_quantidade(nova_quantidade)
                    print("Quantidade atualizada com sucesso!")
                    break
            else:
                print("Produto não encontrado.")
        elif escolha == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")   

if __name__ == "__main__":
    menu()            
