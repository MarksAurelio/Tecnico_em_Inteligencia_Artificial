# A função round() em Python é nativa, mas para garantir
# que o resultado seja sempre arredondado para o inteiro mais próximo,
# o código esqueleto pode incluir uma função específica.
# Usaremos a função round() nativa do Python.

renda = float(input("Digite sua renda em talões: "))
imposto = 0.0

LIMITE_INFERIOR = 85528.0
ALIQUOTA_INFERIOR = 0.18  # 18%
ISENCAO = 556.02
ALIQUOTA_SUPERIOR = 0.32  # 32%
IMPOSTO_BASE_SUPERIOR = 14839.02

# --- Cálculo do Imposto ---

if renda <= LIMITE_INFERIOR:
    # 1. Renda não superior a 85.528 talões
    # Imposto = 18% da renda - 556.02
    imposto = (renda * ALIQUOTA_INFERIOR) - ISENCAO

else:
    # 2. Renda superior a 85.528 talões
    # Imposto = 14.839,02 + 32% do excedente acima de 85.528
    excedente = renda - LIMITE_INFERIOR
    imposto = IMPOSTO_BASE_SUPERIOR + (excedente * ALIQUOTA_SUPERIOR)

# --- Regra de Imposto Negativo ---

# Nota: Se o imposto calculado for menor que zero,
# isso significa nenhum imposto (o imposto é igual a zero).
if imposto < 0:
    imposto = 0.0

# --- Saída do Resultado ---

# O imposto deve ser impresso arredondado para o inteiro mais próximo.
imposto_final_arredondado = round(imposto)

print(f"O imposto calculado é de {imposto_final_arredondado} talões.")
