import streamlit as st

st.set_page_config(
    page_title="SRA MILLONES - Restaurante",
    page_icon="🍽️",
    layout="wide"
)

st.image("images/logo.png", width=150)
st.title("🍽️ Bienvenido a SRA MILLONES")
st.markdown("Seleccione una opción en el menú lateral:")

st.markdown("""
- **Vista del Mozo:** Para registrar pedidos
- **Vista de Admin:** Para ver ventas y exportar
""")
