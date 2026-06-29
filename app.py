import streamlit as st
import pandas as pd

from utils.ranking import obtener_ranking

st.set_page_config(
    page_title="Pádel 2026",
    page_icon="🎾",
    layout="wide"
)

# ==========================
# DATOS
# ==========================

ranking = obtener_ranking()

try:
    partidos = pd.read_csv("data/partidos.csv")
    cantidad_partidos = len(partidos)
except:
    partidos = pd.DataFrame()
    cantidad_partidos = 0

# ==========================
# TITULO
# ==========================

st.title("🎾 Liga de Pádel Heredia")
st.caption("Temporada 2026")

st.divider()

# ==========================
# DASHBOARD
# ==========================

lider = "-"

if not ranking.empty:
    lider = ranking.iloc[0]["Jugador"]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👥 Jugadores", 7)

with col2:
    st.metric("🎾 Partidos", cantidad_partidos)

with col3:
    st.metric("🥇 Líder", lider)

st.divider()

# ==========================
# TOP 3
# ==========================

st.subheader("🏆 Top 3 del Ranking")

if not ranking.empty:

    podio = ranking.head(3)

    cols = st.columns(3)

    medallas = ["🥇", "🥈", "🥉"]

    for i, columna in enumerate(cols):

        jugador = podio.iloc[i]

        with columna:

            st.markdown(f"### {medallas[i]} {jugador['Jugador']}")

            st.metric(
                "Puntos",
                jugador["Puntos"]
            )

            st.metric(
                "Victorias",
                jugador["PG"]
            )

else:

    st.info("Todavía no hay partidos cargados.")

st.divider()

# ==========================
# ÚLTIMOS PARTIDOS
# ==========================

st.subheader("📋 Últimos Partidos")

if cantidad_partidos == 0:

    st.info("Todavía no hay partidos cargados.")

else:

    ultimos = partidos.tail(5).iloc[::-1]

    for _, fila in ultimos.iterrows():

        st.markdown(
            f"""
**📅 {fila['fecha']}**

🎾 **{fila['jugador1']}** + **{fila['jugador2']}**

🆚

🎾 **{fila['jugador3']}** + **{fila['jugador4']}**

🏆 **Ganadores**

✅ **{fila['ganador1']}** + **{fila['ganador2']}**

---
"""
        )