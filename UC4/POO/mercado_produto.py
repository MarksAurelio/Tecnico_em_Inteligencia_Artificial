# Ultimo desafio 
# Criar uma classe Produto com os atributos nome, preco, estoque, data_validade.
# Criar métodos para adicionar estoque, remover estoque e verificar validade.
# Criar uma lista de produtos e listar todos os produtos com seus detalhes.
class Mercado_Produto:
    def __init__(self, nome, preco, quantidade,data_validade=None):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.data_validade = data_validade

    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco

    def atualizar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade

    def verificar_validade(self, data_validade):
        self.data_validade = data_validade

    def __str__(self):
        return f"Produto: {self.nome}, Preço: {self.preco}, Quantidade: {self.quantidade}"
    