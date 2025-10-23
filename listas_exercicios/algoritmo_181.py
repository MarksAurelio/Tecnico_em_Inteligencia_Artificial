# Criar um algoritmo que imprima todos os números de 1 até 100 e a soma deles 
 
soma = 0 
for i in range(1, 101):
    print(i)
    soma = soma + i
print("A soma dos números de 1 a 100 é:", soma)

# Em Streamlit
import streamlit as st

st.title("Soma dos Números de 1 a 100")

# 1. Variáveis de controle
soma = 0
numeros_processados = []

# 2. Loop para contagem e soma
for i in range(1, 101):
    # Armazena o número para exibição posterior
    numeros_processados.append(str(i))
    
    # Realiza a soma cumulativa
    soma = soma + i

# 3. Exibição dos resultados

# Exibe a sequência de números (simulando o 'print(i)')
st.subheader("Números Processados (1 a 100):")
# Junta a lista de números em uma única string para exibição em bloco
st.text("\n".join(numeros_processados))

st.markdown("---")

# Exibe a soma final
st.subheader("Resultado Final:")
st.success(f"A soma dos números de 1 a 100 é: **{soma}**")

# Destaque visual (o valor é 5050)
st.metric(label="Soma Total", value=soma)
