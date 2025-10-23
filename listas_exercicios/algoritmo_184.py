# Entrar com 8 números e, para cada número, imprimir o logaritmo desse número na base 10

import math

for i in range(8):
    try:
        num = float(input("Digite um número: "))
        if num > 0:
            logaritmo = math.log10(num)
            print(f"O logaritmo de {num} na base 10 é {logaritmo}")
        else:
            print("Número inválido. Digite um número positivo.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

# Em Streamlit
import streamlit as st
import math
import pandas as pd

st.title("Cálculo de Logaritmo (Base 10) de 8 Números")

NUM_ENTRADAS = 8

# 1. Inicialização do estado da sessão para armazenar os 8 inputs
if 'inputs_log' not in st.session_state:
    # Inicializa o estado com 8 valores zero
    st.session_state.inputs_log = [1.0] * NUM_ENTRADAS  # Começa com 1.0 para log10 ser 0

st.subheader("Digite 8 Números Positivos:")

# Cria 8 campos de entrada dinamicamente
for i in range(NUM_ENTRADAS):
    # Função de callback para atualizar a lista de inputs no session_state
    def update_input(index=i):
        # Garante que o input no session_state é atualizado
        st.session_state.inputs_log[index] = st.session_state[f'log_num_{index}']

    st.number_input(
        f"Número {i+1}:",
        key=f"log_num_{i}",
        value=st.session_state.inputs_log[i],
        min_value=0.0, # Permite 0 no input, mas a lógica de cálculo irá rejeitar
        format="%.2f",
        on_change=update_input
    )

# 2. Lógica de processamento e exibição

def processar_logaritmo():
    """Calcula o logaritmo de cada número e armazena os resultados."""
    resultados = []
    
    # Itera sobre os valores armazenados no session_state
    for i, num in enumerate(st.session_state.inputs_log):
        logaritmo_resultado = ""
        mensagem = ""
        
        try:
            if num > 0:
                # Caso VÁLIDO: calcula o logaritmo
                logaritmo = math.log10(num)
                logaritmo_resultado = f"{logaritmo:.6f}"
                mensagem = f"Logaritmo na base 10: {logaritmo_resultado}"
            else:
                # Caso Inválido: número menor ou igual a zero
                logaritmo_resultado = "Inválido"
                mensagem = "Número inválido. Digite um número positivo."
        except Exception:
            # Captura outras exceções (como erro de digitação/formato)
            logaritmo_resultado = "Erro"
            mensagem = "Entrada inválida. Por favor, digite um número."
        
        resultados.append({
            "Nº": i + 1,
            "Número Digitado": f"{num:.2f}",
            "Log₁₀": logaritmo_resultado,
            "Status": mensagem
        })
    
    st.session_state.resultados_log_df = pd.DataFrame(resultados)
    st.session_state.processado_log = True # Sinaliza que o cálculo foi feito

st.markdown("---")

# Botão para acionar o cálculo
if st.button("Calcular Logaritmos", on_click=processar_logaritmo):
    pass # A função on_click já faz o trabalho

# 3. Exibição dos resultados processados
if 'processado_log' in st.session_state and st.session_state.processado_log:
    st.subheader("Resultados")
    # Exibe os resultados na forma de tabela
    st.dataframe(st.session_state.resultados_log_df, hide_index=True, use_container_width=True)

    st.markdown("---")
    st.markdown("**Saída sequencial (simulada):**")
    # Simula a saída de console com as mensagens originais
    for _, row in st.session_state.resultados_log_df.iterrows():
        st.markdown(f"- **{row['Número Digitado']}**: {row['Status']}")
