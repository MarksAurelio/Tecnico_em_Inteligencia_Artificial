# Entrar com 10 números e imprimir o quadrado de cada número

for i in range(10):
    num = float(input("Digite um número: "))
    print(f"O quadrado de {num} é {num**2}")

# Em Streamlit
import streamlit as st
import pandas as pd

st.title("Cálculo do Quadrado de 10 Números")

NUM_ENTRADAS = 10

# 1. Inicialização do estado da sessão para armazenar os 10 inputs
if 'inputs_quadrado' not in st.session_state:
    st.session_state.inputs_quadrado = [0.0] * NUM_ENTRADAS

st.subheader("Digite 10 Números:")

# Cria 10 campos de entrada dinamicamente
for i in range(NUM_ENTRADAS):
    # Função de callback para atualizar a lista de inputs no session_state
    def update_input(index=i):
        st.session_state.inputs_quadrado[index] = st.session_state[f'quadrado_num_{index}']
    
    st.number_input(
        f"Número {i+1}:",
        key=f"quadrado_num_{i}",
        value=st.session_state.inputs_quadrado[i],
        format="%.2f",
        on_change=update_input
    )

# 2. Lógica de processamento e exibição

def processar_quadrado():
    """Calcula o quadrado de cada número e armazena os resultados."""
    resultados = []
    
    # Itera sobre os valores armazenados no session_state
    for num in st.session_state.inputs_quadrado:
        quadrado = num ** 2
        resultados.append({
            "Número Digitado": f"{num:.2f}",
            "Quadrado": f"{quadrado:.2f}"
        })
    
    st.session_state.resultados_quadrado_df = pd.DataFrame(resultados)
    st.session_state.processado_quadrado = True # Sinaliza que o cálculo foi feito

st.markdown("---")

# Botão para acionar o cálculo
if st.button("Calcular Quadrados", on_click=processar_quadrado):
    pass # A função on_click já faz o trabalho

# 3. Exibição dos resultados processados
if 'processado_quadrado' in st.session_state and st.session_state.processado_quadrado:
    st.subheader("Resultados")
    # Exibe os resultados na forma de tabela
    st.dataframe(st.session_state.resultados_quadrado_df, hide_index=True, use_container_width=True)

    st.success("Cálculo concluído para todos os 10 números.")

    # Simula a saída do print original de forma sequencial (opcional)
    st.markdown("---")
    st.markdown("**Saída sequencial (simulada):**")
    for _, row in st.session_state.resultados_quadrado_df.iterrows():
        st.markdown(f"O quadrado de {row['Número Digitado']} é **{row['Quadrado']}**")
    