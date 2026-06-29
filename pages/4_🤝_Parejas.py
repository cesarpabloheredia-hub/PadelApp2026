import streamlit as st
import pandas as pd

st.title("🤝 Ranking de Parejas")

try:

    partidos = pd.read_csv("data/partidos.csv")

except:

    st.warning("Todavía no hay partidos cargados.")
    st.stop()

parejas = {}

for _, fila in partidos.iterrows():

    pareja = tuple(sorted([
        fila["ganador1"],
        fila["ganador2"]
    ]))

    parejas[pareja] = parejas.get(
        pareja,
        0
    ) + 1

ranking = pd.DataFrame([
    {
        "Pareja": f"{a} + {b}",
        "Victorias": v
    }

    for (a, b), v in parejas.items()

])

ranking = ranking.sort_values(
    by="Victorias",
    ascending=False
)

ranking.insert(
    0,
    "Pos",
    range(1, len(ranking)+1)
)

st.dataframe(
    ranking,
    hide_index=True,
    use_container_width=True
)

if len(ranking):

    mejor = ranking.iloc[0]

    st.divider()

    st.success(
        f"""
🥇 Mejor pareja actual

{mejor['Pareja']}

🏆 {mejor['Victorias']} victorias
"""
    )