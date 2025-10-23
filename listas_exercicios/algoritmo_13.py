# Confirmar se elemento estar na lista

mercado = ["Ações", "Opções", "Futuro", "Dólar", "Ouro", "Criptmoedas"]

busca = "Futuro" in mercado

print(busca)

# Em Streamlit
import streamlit as st

# A lista de dados
mercado = ["Ações", "Opções", "Futuro", "Dólar", "Ouro", "Criptmoedas"]

# Verificação de existência
busca = "Futuro" in mercado

# Configuração e exibição no Streamlit
st.title("Verificação de Item na Lista")

# Exibindo a lista completa para contexto
st.write("Lista de Mercados:", mercado)

# Exibindo a lógica da busca
st.markdown(f"Verificando se **'Futuro'** está na lista...")

# Exibindo o resultado booleano
if busca:
    st.success(f"Resultado da busca (`'Futuro' in mercado`): **{busca}**")
else:
    st.error(f"Resultado da busca (`'Futuro' in mercado`): **{busca}**")
