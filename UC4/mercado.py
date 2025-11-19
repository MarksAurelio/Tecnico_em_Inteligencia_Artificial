# A classe é u conjunto de objtos
class Mercado:
# Métodos especiais (dunder methods)
# __init__ é o construtor da classe
# Stack e Help
# Stack é a pilha de chamadas
# Heap é a memória dinâmica
# Self serve para definir o atributos do objeto
    def __init__(self, nome, midia, ativo):
        self.nome = nome
        self.midia = midia
        self.ativo = ativo

    def ativar(self):
        self.ativo = True

    def desativar(self):
        self.ativo = False

# Método especial para representar o objeto como string
    def __str__(self):
        return f'O mercado {self.nome}, está {"Ativo" if self.ativo else "Inativo"}'
    
    def listar_mercados():
        pass
