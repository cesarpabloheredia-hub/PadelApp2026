import streamlit as st

from utils.ranking import obtener_ranking

st.title("🏆 Ranking General")

ranking = obtener_ranking()

if ranking.empty:
    st.warning("Todavía no hay partidos cargados.")
    st.stop()

# -----------------------------
# PODIO
# -----------------------------

st.subheader("🥇 Podio")

podio = ranking.head(3)

c1, c2, c3 = st.columns(3)

medallas = ["🥇", "🥈", "🥉"]

for coluna, (_, jugador), medalla in zip(
    [c1, c2, c3],
    podio.iterrows(),
    medallas
):

    with coluna:

        st.markdown(f"## {medalla}")

        st.markdown(f"### {jugador['Jugador']}")

        st.metric(
            "🏆 Puntos",
            jugador["Puntos"]
        )

        st.metric(
            "🥇 Victorias",
            jugador["PG"]
        )

        st.metric(
            "📈 Efectividad",
            f"{jugador['% Éxito']} %"
        )

st.divider()

# -----------------------------
# TABLA
# -----------------------------

st.subheader("📊 Ranking Completo")

tabla = ranking.copy()

tabla.insert(0, "Pos", range(1, len(tabla)+1))

st.dataframe(
    tabla,
    hide_index=True,
    use_container_width=True
)