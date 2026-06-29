import streamlit as st
from utils.ranking import obtener_ranking

st.title("📈 Estadísticas")

ranking = obtener_ranking()

if ranking.empty:
    st.warning("Todavía no hay partidos cargados.")
    st.stop()

# ==========================
# RESUMEN GENERAL
# ==========================

st.subheader("📊 Resumen General")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("👥 Jugadores", len(ranking))

with c2:
    st.metric("🏆 Victorias Totales", ranking["PG"].sum())

with c3:
    st.metric("❌ Derrotas Totales", ranking["PP"].sum())

with c4:
    st.metric(
        "🥇 Líder",
        ranking.iloc[0]["Jugador"]
    )

st.divider()

# ==========================
# TABLA
# ==========================

st.subheader("📋 Estadísticas por Jugador")

tabla = ranking.copy()

tabla = tabla.rename(columns={
    "PJ":"Partidos",
    "PG":"Victorias",
    "PP":"Derrotas",
    "% Éxito":"Efectividad (%)"
})

st.dataframe(
    tabla,
    hide_index=True,
    use_container_width=True
)

st.divider()

# ==========================
# MVP
# ==========================

mvp = ranking.iloc[0]

st.success(
    f"""
🏆 MVP ACTUAL

👤 {mvp['Jugador']}

🥇 {mvp['PG']} victorias

📈 {mvp['% Éxito']} % de efectividad
"""
)