import streamlit as st
import pandas as pd
from datetime import date
import os

st.title("🎾 Registrar Partido")
st.write("APP CARGADA ✔")
JUGADORES = [
    "Pablo Heredia",
    "Flavio Aguirre",
    "Cristian Perez",
    "Armando Perez",
    "Ignacio Perez",
    "Sebastian Gomez",
    "Lautaro Martinez"
]

fecha = st.date_input(
    "📅 Fecha",
    value=date.today()
)

st.divider()

st.subheader("Pareja A")

col1, col2 = st.columns(2)

with col1:
    jugador1 = st.selectbox(
        "Jugador 1",
        JUGADORES,
        key="j1"
    )

with col2:
    disponibles = [j for j in JUGADORES if j != jugador1]

    jugador2 = st.selectbox(
        "Jugador 2",
        disponibles,
        key="j2"
    )

st.divider()

st.subheader("Pareja B")

disponibles = [
    j for j in JUGADORES
    if j not in [jugador1, jugador2]
]

col3, col4 = st.columns(2)

with col3:

    jugador3 = st.selectbox(
        "Jugador 3",
        disponibles,
        key="j3"
    )

with col4:

    disponibles2 = [
        j for j in disponibles
        if j != jugador3
    ]

    jugador4 = st.selectbox(
        "Jugador 4",
        disponibles2,
        key="j4"
    )

st.divider()

ganador = st.radio(
    "🏆 Pareja Ganadora",
    [
        "Pareja A",
        "Pareja B"
    ],
    horizontal=True
)

if st.button("💾 Registrar Partido", use_container_width=True):

    # marcar que se registró el partido
    st.session_state["partido_ok"] = True

# 👇 esto va FUERA del botón (pero justo después en el código)
if "partido_ok" in st.session_state and st.session_state["partido_ok"]:

    st.success("Partido guardado ✔")
    st.toast("✅ Partido registrado correctamente")

    # resetear estado para que no se repita siempre
    st.session_state["partido_ok"] = False