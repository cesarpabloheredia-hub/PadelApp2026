import streamlit as st

from styles.colors import COLORES


def mostrar_player_card(datos):

    color = COLORES.get(
        datos["Jugador"],
        "#3498DB"
    )

    st.markdown(
        f"""
<div style="
background:{color};
padding:18px;
border-radius:18px;
color:white;
margin-bottom:15px;
box-shadow:0px 4px 10px rgba(0,0,0,0.30);
">

<h3 style="margin:0;">
{datos["Jugador"]}
</h3>

<hr>

🏆 <b>{datos["Puntos"]}</b> puntos<br>

🥇 <b>{datos["PG"]}</b> victorias<br>

❌ <b>{datos["PP"]}</b> derrotas<br>

📈 <b>{datos["% Éxito"]}%</b> efectividad

</div>
""",
        unsafe_allow_html=True
    )