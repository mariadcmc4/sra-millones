import streamlit as st
from PIL import Image
import os

# Configuración de la página
st.set_page_config(
    page_title="SRA MILLONES - Restaurante",
    layout="centered"
)

# CSS para alinear logo y texto como en tu ejemplo
st.markdown(
    """
    <style>
    .centered-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .logo-title {
        display: flex;
        flex-direction: row;
        align-items: center; /* Centra verticalmente el texto con el logo */
        gap: 15px;
    }
    .title-text {
        display: flex;
        flex-direction: column;
        justify-content: center; /* Centra el bloque de texto */
    }
    .title-text h1 {
        margin: 0;
        font-size: 2rem;
        font-weight: bold;
    }
    .title-text h3 {
        margin: 0;
        font-weight: normal;
        color: gray;
        font-size: 1.1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Contenedor principal
st.markdown('<div class="centered-container">', unsafe_allow_html=True)

# Fila con logo y texto
st.markdown('<div class="logo-title">', unsafe_allow_html=True)

# Logo
logo_path = os.path.join("images", "logo.jpg")
if os.path.exists(logo_path):
    logo = Image.open(logo_path).resize((90, 90))
    st.image(logo)
else:
    st.warning("⚠ No se encontró el archivo images/logo.jpg")

# Texto
st.markdown(
    """
    <div class="title-text">
        <h1>🍽 SRA MILLONES</h1>
        <h3>Restaurante Criollo</h3>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)  # Cierra logo-title

# Espacio
st.write("")
st.subheader("Iniciar Sesión")
# Añadimos este CSS para que los inputs sean más cortos
st.markdown(
    """
    <style>
    /* Ajustar ancho máximo de las cajas de texto */
    .stTextInput > div > div > input {
        max-width: 250px; /* ancho máximo */
        margin: auto; /* centrado */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Formulario
usuario = st.text_input("Usuario")
password = st.text_input("Contraseña", type="password")

if st.button("Entrar"):
    if usuario and password:
        st.success(f"✅ Bienvenido, {usuario}")
    else:
        st.error("❌ Por favor, ingresa usuario y contraseña.")

# Cierra container
st.markdown('</div>', unsafe_allow_html=True)
