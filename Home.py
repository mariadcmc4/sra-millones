import streamlit as st
from PIL import Image
import json
import os

# Configuración
st.set_page_config(page_title="SRA MILLONES - Restaurante", layout="centered")

# CSS personalizado
st.markdown(
    """
    <style>
    /* Ocultar menú y pie de página */
    #MainMenu, header, footer {visibility: hidden;}

    /* Fondo general */
    .stApp {
        background-color: #f0f2f6;
    }

    /* Centrado vertical */
    .block-container {
        padding-top: 0 !important;
        margin-top: 0 !important;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }

    /* Tarjeta de login */
    .login-card {
        background-color: transparent;
        padding: 30px 40px;
        border-radius: 12px;
        text-align: center;
        max-width: 400px;
        width: 100%;
    }

    /* Logo y título */
    .logo-title {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        margin-bottom: 20px;
    }

    .title-text h1 {
        margin: 0;
        font-size: 1.6rem;
        font-weight: bold;
    }
    .title-text h3 {
        margin: 0;
        font-weight: normal;
        color: gray;
        font-size: 1rem;
    }

    /* Inputs alineados */
    .stTextInput {
     max-width: 250px;
     

    }
    .stTextInput > div > div > input {
        width: 100%;
        max-width: 250px;
        background-color: #ffffff !important;
        border: 1px solid #cccccc;
        border-radius: 8px;
        padding: 4px 10px;
        color: #333333;
       
    }

    /* Botón centrado */
    .stButton {
        display: flex;
        justify-content: center;
        
    }
    .stButton > button {
        background-color: #f8b400;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 8px;
        font-weight: bold;
        cursor: pointer;
       
    }
    .stButton > button:hover {
        background-color: #d99a00;
        
    }

    /* Responsive para móviles */
    @media (max-width: 480px) {
        .login-card {
            padding: 20px;
            max-width: 90%;
        }

        .stTextInput > div > div > input {
            max-width: 250;
            width: 100%;
           
        }

        .logo-title {
            flex-direction: column;
            gap: 10px;
        }

        .title-text h1 {
            font-size: 1.4rem;
        }

        .title-text h3 {
            font-size: 0.9rem;
        }
        /* Evitar que el label se divida en dos líneas */
        label[data-testid="stTextInputLabel"] {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        display: block;
        text-align: left;
        font-weight: bold;
        margin-bottom: 5px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Tarjeta de login
st.markdown('<div class="login-card">', unsafe_allow_html=True)

# Logo y título
st.markdown('<div class="logo-title">', unsafe_allow_html=True)
logo_path = os.path.join("images", "logo.jpg")
if os.path.exists(logo_path):
    logo = Image.open(logo_path).resize((70, 70))
    st.image(logo)
else:
    st.write("⚠ Logo no encontrado")

st.markdown(
    """
    <div class="title-text">
        <h1>🍽 SRA MILLONES</h1>
        <h3>Restaurante Criollo</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Formulario centrado en una sola columna
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    usuario = st.text_input("Usuario", key="usuario_input")
    password = st.text_input("Contraseña", type="password", key="password_input")
    
    st.markdown("<br>", unsafe_allow_html=True)  # Espacio entre inputs y botón

    if st.button("Ingresar"):
        usuarios = cargar_usuarios()
        rol = autenticar(usuario, password, usuarios)

        if rol:
            st.success(f"✅ Bienvenido/a *{usuario}* — Rol: **{rol}**")
            if rol == "Administrador":
                st.info("🔧 Acceso a configuración del sistema")
            elif rol == "Mozo":
                st.info("📝 Acceso a registro de pedidos")
        else:
            st.error("❌ Usuario o contraseña incorrectos")
# Cargar usuarios desde login.json
def cargar_usuarios():
    with open("login.json", "r") as archivo:
        return json.load(archivo)
# Verificar credenciales
def autenticar(usuario, password, lista_usuarios):
    for u in lista_usuarios:
        if u["usuario"] == usuario and u["password"] == password:
            return u["rol"]
    return None
