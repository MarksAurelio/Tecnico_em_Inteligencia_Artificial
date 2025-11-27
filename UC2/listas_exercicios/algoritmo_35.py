""" Enunciado: Ler nome, endereço e telefone e imprimi-los. """

nome = input("Digite seu nome: ")
endereco = input("Digite seu endereço: ")
telefone = input("Digite seu telefone: ")

print("Nome:", nome)
print("Endereço:", endereco)
print("Telefone:", telefone)

# Em Streamlit
import streamlit as st

st.title("Coleta de Dados Pessoais")

# 1. Widgets de entrada de texto
# O valor digitado é armazenado na variável correspondente.
nome = st.text_input("Digite seu nome:", key="nome_input")
endereco = st.text_input("Digite seu endereço:", key="endereco_input")
telefone = st.text_input("Digite seu telefone:", key="telefone_input")

# 2. Exibição dos resultados
st.write("---")

# A exibição só será feita se o campo 'nome' tiver sido preenchido,
# evitando mostrar "Nome: " quando o app carrega pela primeira vez.
if nome and endereco and telefone:
    st.subheader("Dados Digitados:")
    st.markdown(f"**Nome:** {nome}")
    st.markdown(f"**Endereço:** {endereco}")
    st.markdown(f"**Telefone:** {telefone}")
elif nome or endereco or telefone:
    # Mostra uma mensagem se o usuário começou a digitar, mas não terminou
    st.info("Preencha todos os campos para visualizar os dados.")
else:
    # Mensagem inicial
    st.caption("Aguardando a digitação dos dados...")
