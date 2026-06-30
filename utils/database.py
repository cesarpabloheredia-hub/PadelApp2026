from supabase import create_client
import streamlit as st

# Leer credenciales desde Streamlit Secrets
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

# Crear cliente
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def guardar_partido(datos):
    """
    Guarda un partido en la tabla 'partidos'
    """
    return supabase.table("partidos").insert(datos).execute()


def obtener_partidos():
    """
    Devuelve todos los partidos registrados
    """
    respuesta = supabase.table("partidos").select("*").execute()

    if respuesta.data:
        return respuesta.data

    return []


def borrar_todo():
    """
    Elimina todos los partidos
    """
    return supabase.table("partidos").delete().neq("id", 0).execute()