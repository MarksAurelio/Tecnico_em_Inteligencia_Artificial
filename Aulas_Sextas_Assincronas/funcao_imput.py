# O print não tem um resultado utilizável
# O input tem e o nome dessa funçao já diz tudo 
# A função input() em Python é usada para receber entrada do usuário.
# Ela pausa a execução do programa e espera que o usuário digite algo no console.
# O valor digitado pelo usuário é retornado como uma string.        
# nome = input("Digite seu nome: ")
# print("Olá, " + nome + "! Seja bem-vindo(a)!")

# Praticamente todas as linguagens de programação possuem uma função semelhante ao input() do Python,
# embora o nome e a sintaxe possam variar. Por exemplo:
# Em JavaScript, a função equivalente é prompt():
# let nome = prompt("Digite seu nome:");
# Em Java, você pode usar a classe Scanner para obter entrada do usuário:
# import java.util.Scanner;
# Scanner scanner = new Scanner(System.in);
# System.out.print("Digite seu nome: ");
# String nome = scanner.nextLine();
# Em C, você pode usar a função scanf():
# char nome[50];
# printf("Digite seu nome: ");
# scanf("%s", nome);
# Em Ruby, você pode usar gets.chomp:
# puts "Digite seu nome:"
# nome = gets.chomp
# Em todas essas linguagens, a função serve para o mesmo propósito: obter entrada do usuário durante a execução do programa.
# Exemplo em Python:  
# print("Conta-me qualquer coisa...")
# qualquer_coisa = input()
# print("Hum...", qualquer_coisa, "... Realmente?")
# Quando um programa não recebe uma entrada do usário, podemos dizer que ele é um programa "batch" ou "não interativo", ou mesmo que ele é um programa surdo. 
# Essa inserção de dados pode ser do teclado, por voz ou imagem

# input() # sem argumentos faz o programa esperar até que o usuário pressione Enter, mas não armazena nenhum valor. esse uso é raro. e você não verá isso com frequência em códigos reais. além do mais, não é uma boa prática deixar o código assim, pois pode confundir quem for ler o código depois. e os dados assim não são aproveitados, eles são perdidos. 

# A função input() é invocada com um argumento ‒ é uma string contendo uma mensagem; e esse resultado é armazenado em uma variável e é sempre uma string. Uma string contendo todos os caracteres que o usuário insere no teclado. Não é um inteiro ou um float
# ano_atual = input("Qual o ano atual: ")
# print("O ano atual é: " + ano_atual)

# ano_atual = int(input("Qual o ano atual: "))
# print("O ano atual é: ", ano_atual)

# # Exemplo
# numero = input("Digite um número: ")
# potencia = numero ** 2.0
# print(numero, "elevado a 2 é", potencia)
# # O código acima resultará em um erro, porque o valor retornado por input() é uma string. 

# numero = float(input("Digite um número: "))
# potencia = numero ** 2.0
# print(numero, "elevado a 2 é", potencia)
# # Agora esse código tá certo
# # Ter uma equipe composta por três input()-int()-float() abre muitas novas possibilidades.

# # Operadores de string operadores aritméticos: + e *
# # Eles são capazes de fazer algo mais do que apenas adicionar e multiplicar.

# primeiro_nome = input("Posso ter seu primeiro nome, por favor? ")
# sobrenome = input("Posso ter seu sobrenome, por favor? ")
# print("Obrigado!.")
# print("\nSeu nome é " + primeiro_nome + " " + sobrenome + ".")

print("o" + 5 * "-" + "o" + 5 * "-" + "o")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("o" + 10 * "-" + "o")

# meu_input = input("Entre com uma palavra: ") # Exemplo de entrada: Olá
# print(meu_input * 3) # Saída: OláOláOlá

# # Uso str() para converter outros tipos em string
# ano = 2025
# print("Eu tenho " + str(ano) + " anos.")

# ano = input("Em que ano estamos? ")
# print("A palavra 2025 vai se repetir 3 vezes e ficar emendada: ", ano * 3 , ".")

# # Exercicio
# a = float(input("Entre com o primeiro valor: "))
# b = float(input("Entre com o segundo valor: "))
# print("Adição:", a + b,
#       "\nSubtração:", a - b,  # Faltava uma vírgula aqui
#       "\nMultiplicação:", a * b, # E aqui
#       "\nDivisão:", a / b)
# print("\nFim do programa!")

# A função print() envia dados para o console, enquanto a função input() obtém dados do console.
