import streamlit as st

st.title("🧪 Test Supabase")

try:
    import utils.database as db

    st.success("✅ Se importó database.py correctamente")

    if st.button("Probar conexión"):
        respuesta = db.probar_conexion()
        st.success("Conexión OK")
        st.write(respuesta.data)

except Exception as e:
    st.exception(e)