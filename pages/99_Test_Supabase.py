import streamlit as st
from utils.database import probar_conexion

st.title("🧪 Test Supabase")

if st.button("Probar conexión"):

    try:
        respuesta = probar_conexion()
        st.success("✅ Conexión correcta")
        st.write(respuesta.data)

    except Exception as e:
        st.error(e)