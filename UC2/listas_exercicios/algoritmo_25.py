# Crie um menu de opções 
# match case

""" 
append(): adicionar um elemento na lista
clear(): limpar lista
count(): conta quantos elementos têm a lista
extend(): insere uma liste em uma lista
index(): retorna o valor do índice
insert(pos, x)
remove()
reverse()
sort()

... entre outras """

# Estrutura de condição ou seleção 
# if
# if else
# if elif else
# match case

""" 
Create (Criar)
Read (Ler/Visualizar)
Update (Atualizar/Editar)
Delete (Excluir/Deletar)
"""

print("Sistema Barbearia")
clientes = []
cont = True
while cont:
    print("Sistema de Gerenciamento da Barbearia")
    print("1. Agendar Cliente (CREATE)")
    print("2. Visualizar Agendamento (READ)")
    print("3. Atualizar Agendamento (UPDATE)")
    print("4. Cancelar Agendamento (DELETE)")
    print("5. Sair")

    opcao = int(input("Digite uma opção: "))

    match opcao:
        case 1:
            nome = input("Digite seu nome: ")
            clientes.append(nome)
        case 5:
            cont = False

    print(clientes)

# Em Streamlit
    import streamlit as st

# 1. INICIALIZAÇÃO DO ESTADO DA SESSÃO (Session State)
# O st.session_state armazena dados que persistem entre as interações.
if 'clientes' not in st.session_state:
    st.session_state.clientes = []

# --- 2. FUNÇÕES DE CALLBACK (Ações que ocorrem após o clique) ---

def agendar_cliente():
    """Adiciona o nome do campo de texto à lista de clientes."""
    nome = st.session_state.novo_cliente
    if nome and nome.strip() != "":
        st.session_state.clientes.append(nome.strip())
        # Limpa o campo de texto após a adição
        st.session_state.novo_cliente = ""
        st.success(f"Cliente '{nome}' agendado com sucesso!")
    else:
        st.warning("Por favor, digite um nome válido.")

# --- 3. CONSTRUÇÃO DA INTERFACE (Apresentação dos dados e widgets) ---

st.title("Sistema de Gerenciamento da Barbearia")
st.header("Agendamento de Clientes (CRUD Básico)")

# --- Agendar Cliente (CREATE) ---
st.subheader("1. Agendar Cliente (CREATE)")

# Campo de entrada de texto
# O 'key' é usado para acessar o valor digitado via st.session_state
st.text_input("Digite o nome do cliente:", key="novo_cliente")

# Botão de agendamento que chama a função de callback
st.button("Agendar", on_click=agendar_cliente)


# --- Visualizar Agendamento (READ) ---
st.subheader("2. Agendamentos Atuais")

if st.session_state.clientes:
    # Exibe a lista de clientes como uma tabela ou lista
    st.dataframe(st.session_state.clientes, use_container_width=True, hide_index=True)
    st.markdown(f"**Total de Agendamentos:** {len(st.session_state.clientes)}")
else:
    st.info("Nenhum cliente agendado no momento.")

# --- Sair (No Streamlit, 'Sair' geralmente significa parar o script ou resetar) ---
st.markdown("---")
# Para simular o 'Sair', podemos adicionar um botão para resetar a lista.
if st.button("Resetar Agendamentos (Simular Saída/Limpeza)"):
    st.session_state.clientes = []
    st.experimental_rerun() # Recarrega o script para refletir o reset
