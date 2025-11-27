ano = int(input("Digite o número do ano: "))

# A lógica de anos bissextos é implementada através de condições aninhadas (if/elif/else)
# seguindo exatamente as regras fornecidas.

if ano % 4 != 0:
    # Regra 1: se o número do ano não é divisível por quatro, é um ano comum
    print(f"O ano {ano} é um ano comum.")
    
elif ano % 100 != 0:
    # Regra 2: caso contrário (já sabemos que é divisível por 4),
    # se o número do ano não for divisível por 100, será um ano bissexto.
    print(f"O ano {ano} é um ano bissexto.")
    
elif ano % 400 != 0:
    # Regra 3: caso contrário (já sabemos que é divisível por 4 e 100),
    # se o número do ano não for divisível por 400, é um ano comum.
    print(f"O ano {ano} é um ano comum.")
    
else:
    # Regra 4: caso contrário (é divisível por 4, 100 e 400),
    # é um ano bissexto.
    print(f"O ano {ano} é um ano bissexto.")
    