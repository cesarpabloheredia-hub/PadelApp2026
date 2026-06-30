from supabase import create_client
import streamlit as st

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def probar_conexion():
    return supabase.table("partidos").select("*").limit(1).execute()

def guardar_partido(datos):
    return supabase.table("partidos").insert(datos).execute()

def obtener_partidos():
    respuesta = (
        supabase
        .table("partidos")
        .select("*")
        .order("id")
        .execute()
    )

    return respuesta.data

def borrar_todo():
    return supabase.table("partidos").delete().neq("id", 0).execute()