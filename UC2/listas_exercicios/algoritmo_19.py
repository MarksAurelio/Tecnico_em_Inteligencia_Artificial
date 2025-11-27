# Reverse

mercado = ["Ações", "opções", "Futuro", "Dólar", "Ouro", "criptmoedas"]
mercado.reverse()

lista_reserva_case_insensitive = sorted(mercado, key=str.lower)
print("Minha lista decrescente", mercado)

# Em Streamlit
import streamlit as st

# Lista original
mercado = ["Ações", "opções", "Futuro", "Dólar", "Ouro", "criptmoedas"]

st.title("Reversão e Ordenação de Listas")

st.subheader("1. Lista Original")
st.code(mercado)

# --------------------------
# Operação de Reversão
# --------------------------
# Reverte a lista original INPLACE (modifica 'mercado')
mercado.reverse()

st.subheader("2. Lista Após Reversão (mercado.reverse())")
# Exibindo a lista revertida
st.warning(f"Minha lista decrescente (revertida): {mercado}")
st.caption("Atenção: `.reverse()` apenas inverte a ordem atual, não ordena alfabeticamente.")


# --------------------------
# Operação de Ordenação (sorted)
# --------------------------
# Cria uma NOVA lista ordenada de forma case-insensitive,
# mas não a exibe no print original, então a exibimos aqui
lista_reserva_case_insensitive = sorted(mercado, key=str.lower)

st.subheader("3. Lista Ordenada Case-Insensitive (Usando sorted())")
st.info(f"Lista de Reserva (ordenada): {lista_reserva_case_insensitive}")
st.caption("Esta nova lista não foi modificada pelo `.reverse()`.")
