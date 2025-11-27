# Entrar com 10 números e imprimir a metade de cada número

for i in range(10):
    num = float(input("Digite um número: "))
    metade = num / 2
    print(f"A metade de {num} é {metade}")
    
# Em Streamlit
import streamlit as st
import pandas as pd

st.title("Cálculo da Metade de 10 Números")

NUM_ENTRADAS = 10

# 1. Criação e coleta dos widgets de entrada
# Usamos o st.session_state para garantir que os inputs sejam armazenados
if 'inputs' not in st.session_state:
    # Inicializa o estado com 10 valores zero
    st.session_state.inputs = [0.0] * NUM_ENTRADAS

st.subheader("Digite 10 Números:")

# Cria 10 campos de entrada dinamicamente
for i in range(NUM_ENTRADAS):
    # A função de callback 'on_change' atualiza a lista de inputs no session_state
    def update_input(index=i):
        st.session_state.inputs[index] = st.session_state[f'num_{index}']
    
    st.number_input(
        f"Número {i+1}:",
        key=f"num_{i}",
        value=st.session_state.inputs[i],
        format="%.2f",
        on_change=update_input
    )

# 2. Lógica de processamento e exibição

def processar_calculo():
    """Calcula a metade de cada número e armazena os resultados."""
    resultados = []
    
    # Itera sobre os valores armazenados no session_state
    for num in st.session_state.inputs:
        metade = num / 2
        resultados.append({
            "Número Digitado": f"{num:.2f}",
            "Metade": f"{metade:.2f}"
        })
    
    st.session_state.resultados_df = pd.DataFrame(resultados)
    st.session_state.processado = True # Sinaliza que o cálculo foi feito

st.markdown("---")

# Botão para acionar o cálculo
if st.button("Calcular Metades", on_click=processar_calculo):
    pass # A função on_click já faz o trabalho

# 3. Exibição dos resultados processados
if 'processado' in st.session_state and st.session_state.processado:
    st.subheader("Resultados")
    # Exibe os resultados na forma de tabela
    st.dataframe(st.session_state.resultados_df, hide_index=True, use_container_width=True)

    st.success("Cálculo concluído para todos os 10 números.")

    # Simula a saída do print original de forma sequencial (opcional)
    st.markdown("---")
    st.markdown("**Saída sequencial (simulada):**")
    for _, row in st.session_state.resultados_df.iterrows():
        st.markdown(f"A metade de {row['Número Digitado']} é {row['Metade']}")
        