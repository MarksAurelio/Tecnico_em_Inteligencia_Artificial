"""
Previsão = 10 mil km²
Dimensão do campo de futebol: 100 metros
Como o campo de futebol não pode ser quadrado vamos considerar:
100m x 60m
Digite  a área de desmatamento: 
Area desmatada: xxxxx
Equivalente  a xxxxx campos de futebol (arrendondado) - use funcao round( )
Mas precisamente :   xxxxxxx campos

use as funções: pow(2,2) e round( ) ou o operador ** """
print('Conversor de Desmatamento')

comprimento = 100
largura = 60
area_campo_m2 = comprimento * largura
area_desmatada_km2 = 10000
area_desmatada_m2 = area_desmatada_km2 * (1000**2)
area_total_desmatada = area_desmatada_m2 / area_campo_m2
print(f"A área total desmatada de {area_desmatada_km2:,.0f} Km² equivale a: ")
print(f'{area_total_desmatada:,.0f} campos de futebol.')
