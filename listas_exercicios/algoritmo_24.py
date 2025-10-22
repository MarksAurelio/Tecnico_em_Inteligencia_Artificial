# Fatiar em intervalos

ibovespa = ["PETR4", "BBAS3", "USIMS", "GGBR4", "VALE3"]
# O elemento de índice 2 ao índice 3
print(ibovespa[2:4])
# O elemento do índice 1 até o último 
print(ibovespa[1:])
# Do elemento inicial (zero) ao elemento 2 ()
print(ibovespa[:3])
# Do elemento inicial ao último saltando de 2 em 2
print(ibovespa[0:5:2])
# Selecionar os três últimos elementos da lista
print(ibovespa[-3:])
# Selecionar os 2 primeiros elementos da lista
print(ibovespa[:-3])
