# Imprimir mensagem

print("Você só aprende a programar, programando! Dennis M. Ritchie, criador da linguagem C")

# Em Streamlit
import streamlit as st

# A citação
citacao = "Você só aprende a programar, programando! Dennis M. Ritchie, criador da linguagem C"

st.title("Citação Inspiradora sobre Programação")

# Exibindo a citação com destaque de formatação
st.markdown(f"**_\"{citacao}\"_**")

# Para dar ainda mais destaque, você pode usar um bloco de código ou um expander:
with st.expander("Ver a Citação em Destaque"):
    st.code(citacao)
    st.caption("— Dennis M. Ritchie, criador da linguagem C")
