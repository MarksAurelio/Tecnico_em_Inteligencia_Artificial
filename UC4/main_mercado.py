from mercado import Mercado
# Se eu programo sem Orientação a Objetos, eu sou programador procedural
# Funções soltas, estruturas sequênciais e dicionários

# Criar um dicionário mercado, nome, site, ativo
mercado = {
    "nome": "Tudo Bom",
    "midia": "www.tudobom.com.br",
    "ativo": False
}
# Paradigma Procedural
# Paradigma Orientado a Objetos
# Paradigma Funcional

m1 = Mercado("Tudo Bom", "www.tudobom.com.br", False)
m2 = Mercado("Compra fácil", "www.comprafacil.com.br", True)
m3 = Mercado("Mercado Legal", "www.mercadolegal.com.br", False)
m4 = Mercado("Supermercado Show", "www.supermercadoshow.com.br", True)

print(m1.ativo)
m1.ativar()
print(m1.ativo)
m1.desativar()
print(m1.ativo)

mercados = [m1, m2, m3, m4]
dir(mercados[0])
print("Lista de Mercados: ")
for mercado in mercados:
    status = "Ativo" if mercado.ativo else "Inativo"
    print(f"{mercado.nome}, Site: {mercado.midia}, Status: {status}")

print(vars(m1))
print(dir(m1))
print(m1) # Chama o método __str__ implicitamente
