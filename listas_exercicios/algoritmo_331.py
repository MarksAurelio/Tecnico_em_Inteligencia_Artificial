""" Um marciano chegou a uma floresta e se escondeu atrás de uma
das 100 árvore quando viu um caçador. O caçador só tinha cinco balas em sua
espingarda. Cada vez que ele atirava, e não acertava, é claro, o marciano dizia:
estou mais à direita ou mais à esquerda. Se o caçador não conseguir acertar o
marciano, ele será levado para Marte. Implementar este jogo para dois jogadores,
onde um escolhe a árvore em que o marciano irá se esconder, e o outro tenta acertar """

import random
import pandas as pd

""" Teste 5, para esse teste vou usar a biblioteca random, onde os números vão ser aleatórios. O jogo terá 2 jogadores, um digita o número para o outro adivinhar. """

arvore_marciano = random.randint(1, 100)

tentativas = 5

for i in range(tentativas):
    try:
        chute_cacador = int(input(f"Caçador, você tem {tentativas - i} bala(s). Adivinhe o número da árvore: "))
        
        if chute_cacador == arvore_marciano:
            print("Você acertou! O marciano foi capturado.")
            break
        elif chute_cacador < arvore_marciano:
            print("O marciano disse: 'Estou mais à direita!'")
        else:
            print("O marciano disse: 'Estou mais à esquerda!'")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

else: # Este 'else' é executado se o loop terminar sem 'break'
    print(f"As balas acabaram. O marciano te abduziu!")
    print(f"O marciano estava escondido na árvore: {arvore_marciano}")

# Em Streamlit
import streamlit as st
import random

st.title("Caçada ao Marciano 👽 (Jogo de Adivinhação)")

# --- 1. INICIALIZAÇÃO DO ESTADO DA SESSÃO ---

# arvore_marciano: O número secreto a ser adivinhado
if 'arvore_marciano' not in st.session_state:
    st.session_state.arvore_marciano = None

# tentativas_restantes: O contador de balas (tentativas)
if 'tentativas_restantes' not in st.session_state:
    st.session_state.tentativas_restantes = 5

# jogo_terminado: Flag para saber se o jogo acabou
if 'jogo_terminado' not in st.session_state:
    st.session_state.jogo_terminado = False

# Historico: Armazena as tentativas para reexibir
if 'historico' not in st.session_state:
    st.session_state.historico = []

# --- 2. FUNÇÕES DE CALLBACK ---

def iniciar_jogo(numero_secreto=None):
    """Reseta o jogo com um novo número secreto."""
    if st.session_state.input_secreto and st.session_state.input_secreto > 0 and st.session_state.input_secreto <= 100:
        st.session_state.arvore_marciano = int(st.session_state.input_secreto)
    else:
        # Se o número não for válido ou for deixado em branco, usa um número aleatório (opcional)
        st.session_state.arvore_marciano = random.randint(1, 100)

    st.session_state.tentativas_restantes = 5
    st.session_state.jogo_terminado = False
    st.session_state.historico = []
    st.session_state.ultima_mensagem = "Jogo pronto! Caçador, comece a atirar (1 a 100)."

def tentar_chute():
    """Processa a tentativa do Caçador."""
    if st.session_state.jogo_terminado:
        st.session_state.ultima_mensagem = "O jogo acabou! Inicie um novo."
        return

    chute = st.session_state.chute_cacador
    alvo = st.session_state.arvore_marciano

    if chute is None:
        st.session_state.ultima_mensagem = "Por favor, digite um número."
        return

    st.session_state.tentativas_restantes -= 1

    if chute == alvo:
        st.session_state.ultima_mensagem = "🎯 Você acertou! O marciano foi capturado!"
        st.session_state.jogo_terminado = True
        resultado = "ACERTOU"
    elif st.session_state.tentativas_restantes == 0:
        st.session_state.ultima_mensagem = f"💥 As balas acabaram. O marciano te abduziu! Ele estava em: {alvo}"
        st.session_state.jogo_terminado = True
        resultado = "PERDEU"
    elif chute < alvo:
        st.session_state.ultima_mensagem = "➡ O marciano disse: 'Estou mais à **direita**!'"
        resultado = "DIREITA"
    else:
        st.session_state.ultima_mensagem = "⬅ O marciano disse: 'Estou mais à **esquerda**!'"
        resultado = "ESQUERDA"

    st.session_state.historico.append({
        "Chute": int(chute),
        "Mensagem": st.session_state.ultima_mensagem,
        "Resultado": resultado
    })

# --- 3. INTERFACE DE CONTROLE (MARCIANO) ---

st.subheader("1. Configurar Jogo (Marciano)")
st.caption("O jogador 'Marciano' deve digitar o número secreto e iniciar o jogo.")

col_input, col_btn = st.columns([2, 1])

# Campo de número secreto. Use text_input para que o Marciano possa pedir ao Caçador para olhar para o lado.
col_input.number_input(
    "Digite o número secreto (1 a 100):",
    key="input_secreto",
    min_value=1,
    max_value=100,
    step=1,
    value=50 # Valor padrão
)

col_btn.button(
    "Iniciar Novo Jogo",
    on_click=iniciar_jogo,
    type="primary"
)

# --- 4. INTERFACE DO JOGO (CAÇADOR) ---

st.markdown("---")
st.subheader("2. Adivinhar Número (Caçador)")

if st.session_state.arvore_marciano is None:
    st.warning("Marciano, configure o número secreto e clique em 'Iniciar Novo Jogo'.")
else:
    # Exibe o status atual
    st.metric(
        "Balas Restantes:",
        st.session_state.tentativas_restantes,
        delta_color="off"
    )
    
    # Campo de chute e botão
    col_chute, col_atirar = st.columns([2, 1])
    
    col_chute.number_input(
        f"Caçador, chute o número (1 a 100):",
        key="chute_cacador",
        min_value=1,
        max_value=100,
        step=1,
        disabled=st.session_state.jogo_terminado
    )
    
    col_atirar.button(
        "Atirar!",
        on_click=tentar_chute,
        disabled=st.session_state.jogo_terminado
    )

    # Exibição da última mensagem (dica do Marciano)
    if 'ultima_mensagem' in st.session_state:
        if st.session_state.jogo_terminado:
            st.success(st.session_state.ultima_mensagem) if st.session_state.tentativas_restantes > 0 else st.error(st.session_state.ultima_mensagem)
        else:
            st.info(st.session_state.ultima_mensagem)

    # Histórico de tentativas
    if st.session_state.historico:
        st.markdown("---")
        st.subheader("Histórico de Disparos")
        df_historico = pd.DataFrame(st.session_state.historico)
        st.dataframe(df_historico, hide_index=True, use_container_width=True)
