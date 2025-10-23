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

# Em Streamlit
import streamlit as st

# A lista de dados
ibovespa = ["PETR4", "BBAS3", "USIMS", "GGBR4", "VALE3"]

st.title("Fatiamento de Listas (Slicing)")

st.subheader("Lista Original")
st.code(ibovespa)

st.markdown("---")

# 1. O elemento de índice 2 ao índice 3 (Exibe índice 2 e 3)
fatia1 = ibovespa[2:4]
st.write("**:green[ibovespa[2:4]]** (Índice 2 e 3):", fatia1)

# 2. O elemento do índice 1 até o último
fatia2 = ibovespa[1:]
st.write("**:green[ibovespa[1:]]** (Do índice 1 ao final):", fatia2)

# 3. Do elemento inicial (zero) ao elemento 2 (Exibe índice 0, 1 e 2)
fatia3 = ibovespa[:3]
st.write("**:green[ibovespa[:3]]** (Do início até o índice 2):", fatia3)

# 4. Do elemento inicial ao último saltando de 2 em 2
fatia4 = ibovespa[0:5:2]
st.write("**:green[ibovespa[0:5:2]]** (Do início ao fim, pulando de 2 em 2):", fatia4)

st.markdown("---")

# 5. Selecionar os três últimos elementos da lista
fatia5 = ibovespa[-3:]
st.write("**:blue[ibovespa[-3:]]** (Os 3 últimos elementos):", fatia5)

# 6. Selecionar os 2 primeiros elementos da lista (do início até o antepenúltimo)
fatia6 = ibovespa
