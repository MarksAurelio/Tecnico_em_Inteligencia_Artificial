""" Um marciano chegou a uma floresta e se escondeu atrás de uma
das 100 árvore quando viu um caçador. O caçador só tinha cinco balas em sua
espingarda. Cada vez que ele atirava, e não acertava, é claro, o marciano dizia:
estou mais à direita ou mais à esquerda. Se o caçador não conseguir acertar o
marciano, ele será levado para Marte. Implementar este jogo para dois jogadores,
onde um escolhe a árvore em que o marciano irá se esconder, e o outro tenta acertar """

import random

""" Teste 5, para esse teste vou usar a biblioteca random, onde os números vão ser aleatórios. O jogo terá 2 jogadores, um digita o número para o outro adivinhar. """

arvore_marciano = random.randint(1, 100)

tentativas = 5

for i in range(tentativas):
    try:
        chute_cacador = int(input(f"Caçador, você tem {tentativas - i} bala(s). Adivinhe o número da árvore: "))
        
        if chute_cacador == arvore_marciano:
            print("Você acertou! O marciano foi capturado.")
            break
        elif chute_cacador < arvore_marciano:
            print("O marciano disse: 'Estou mais à direita!'")
        else:
            print("O marciano disse: 'Estou mais à esquerda!'")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

else: # Este 'else' é executado se o loop terminar sem 'break'
    print(f"As balas acabaram. O marciano te abduziu!")
    print(f"O marciano estava escondido na árvore: {arvore_marciano}")
