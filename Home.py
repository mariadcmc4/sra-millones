import streamlit as st
from PIL import Image
import datetime

# Configuración de la página
st.set_page_config(
    page_title="SRA MILLONES - Restaurante",
    page_icon="🍽️",
    layout="wide"
)

# Cargar el logo
logo = Image.open("images/logo.jpg")

# Encabezado
col1, col2 = st.columns([1, 3])
with col1:
    st.image(logo, width=120)
with col2:
    st.title("Restaurante SRA MILLONES")
    st.subheader("Sistema de Pedidos y Ventas")

# Separador
st.markdown("---")

# Descripción
st.write("""
Bienvenido al sistema del restaurante **SRA MILLONES**.  
Aquí podrás:
- Registrar pedidos como mozo/a.
- Administrar ventas, precios y productos como administrador.
""")

# Mostrar fecha y hora actual
st.info(f"📅 Hoy es {datetime.date.today().strftime('%d/%m/%Y')} - ⏰ {datetime.datetime.now().strftime('%H:%M')}")

# Instrucciones rápidas
st.markdown("### 🔹 Cómo usar la app")
st.markdown("""
1. Desde el menú lateral, selecciona **Mozo** para registrar pedidos.
2. Selecciona **Administrador** para ver ventas, cambiar precios o exportar datos.
3. Todos los cambios se guardan automáticamente.
""")

st.success("✅ Selecciona una opción en el menú lateral para comenzar.")
