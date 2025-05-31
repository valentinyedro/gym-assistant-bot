import streamlit as st
from backend import handle_query
from data_loader import load_data
from vector_store import initialize_vector_store

# Configuración de la página y estilos personalizados
st.set_page_config(page_title="Gym Assistant Bot", page_icon="🤖")

# Inicializar datos y vector store
print("Iniciando carga de datos...")
data = load_data()
if data:
    print("Datos cargados correctamente")
    vector_store = initialize_vector_store(data)
    print("Vector store inicializado correctamente")
else:
    print("Error al cargar los datos")

# Agregar CSS personalizado
st.markdown("""
    <style>
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.8rem;
        margin-bottom: 1.5rem;
        line-height: 1.8;
        font-size: 16px;
    }
    .bot-message {
        background-color: #2E2E2E;
        color: #FFFFFF;
    }
    .user-message {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .message-content {
        white-space: pre-line;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        letter-spacing: 0.5px;
        margin-top: 0.5rem;
    }
    .message-content ul {
        list-style-type: none;
        padding-left: 0;
    }
    .message-content li {
        margin-bottom: 0.5rem;
    }
    .emoji {
        font-size: 1.2em;
        margin-right: 0.5rem;
        vertical-align: middle;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Gym Assistant Bot 🤖")

# Inicializar historial en la sesión
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "bot", 
        "content": """¡Bienvenido a DreamGym! 🏋️‍♂️

Soy el asistente virtual especializado en fitness, específicamente programado para DreamGym. Mi expertise incluye:

• 🎯 Asesoramiento sobre programas de entrenamiento
• 📅 Información de clases y horarios
• 💪 Planes de membresía personalizados
• 👨‍🏫 Perfiles de entrenadores expertos
• 🥗 Servicios de nutrición y bienestar

¿En qué aspecto de tu journey fitness puedo ayudarte hoy?"""
    }]

# Input del usuario
user_input = st.chat_input("Escribe tu mensaje aquí...")

# Procesar mensaje del usuario
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = handle_query(user_input, st.session_state.messages)
    st.session_state.messages.append({"role": "bot", "content": response})

# Mostrar historial del chat con mejor formato
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"""
        <div class="chat-message user-message">
            <b>Tu: </b>
            <div class="message-content">
                {message["content"]}
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message bot-message">
            <b>GymBot: </b>
            <div class="message-content">
                {message["content"]}
            </div>
        </div>
        """,unsafe_allow_html=True)