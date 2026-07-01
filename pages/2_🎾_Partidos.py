import streamlit as st
from datetime import date

from utils.database import guardar_partido, borrar_todo

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

    st.session_state["partido_ok"] = True

    if ganador == "Pareja A":
        ganador1 = jugador1
        ganador2 = jugador2
    else:
        ganador1 = jugador3
        ganador2 = jugador4

try:
    guardar_partido({
        "fecha": str(fecha),
        "jugador1": jugador1,
        "jugador2": jugador2,
        "jugador3": jugador3,
        "jugador4": jugador4,
        "ganador1": ganador1,
        "ganador2": ganador2
    })

except Exception as e:
    st.exception(e)

    try:
        guardar_partido({
            "fecha": str(fecha),
            "jugador1": jugador1,
            "jugador2": jugador2,
            "jugador3": jugador3,
            "jugador4": jugador4,
            "ganador1": ganador1,
            "ganador2": ganador2
        })

    except Exception as e:
        st.exception(e)

if st.session_state.get("partido_ok"):

    st.success("✔ Partido registrado correctamente")
    st.toast("🎾 Partido guardado")

    st.session_state["partido_ok"] = False

st.divider()

st.subheader("🔒 Área de Administrador")

password = st.text_input(
    "Contraseña de administrador",
    type="password"
)

if password:

    if password == "PadelSL2026":

        st.success("✅ Acceso autorizado")

        confirmar = st.checkbox(
            "⚠️ Confirmo que deseo eliminar TODOS los partidos y estadísticas."
        )

        if confirmar:

            if st.button("🧹 BORRAR TODO", type="primary"):

                try:
                    borrar_todo()

                    st.success("✅ Todos los partidos fueron eliminados.")
                    st.toast("🧹 Base de datos reiniciada")

                except Exception as e:
                    st.exception(e)

    else:

        st.error("❌ Contraseña incorrecta")