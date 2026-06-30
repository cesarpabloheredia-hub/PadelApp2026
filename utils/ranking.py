import pandas as pd
from utils.database import obtener_partidos

JUGADORES = [
    "Pablo Heredia",
    "Flavio Aguirre",
    "Cristian Perez",
    "Armando Perez",
    "Ignacio Perez",
    "Sebastian Gomez",
    "Lautaro Martinez"
]


def obtener_ranking():

    partidos = obtener_partidos()

    if len(partidos) == 0:
        return pd.DataFrame()

    partidos = pd.DataFrame(partidos)

    ranking = []

    for jugador in JUGADORES:

        victorias = (
            (partidos["ganador1"] == jugador).sum()
            +
            (partidos["ganador2"] == jugador).sum()
        )

        jugados = (
            (partidos["jugador1"] == jugador).sum()
            +
            (partidos["jugador2"] == jugador).sum()
            +
            (partidos["jugador3"] == jugador).sum()
            +
            (partidos["jugador4"] == jugador).sum()
        )

        derrotas = jugados - victorias

        puntos = victorias * 3

        efectividad = 0

        if jugados > 0:
            efectividad = round((victorias / jugados) * 100, 1)

        ranking.append({
            "Jugador": jugador,
            "PJ": jugados,
            "PG": victorias,
            "PP": derrotas,
            "Puntos": puntos,
            "% Éxito": efectividad
        })

    df = pd.DataFrame(ranking)

    df = df.sort_values(
        by=["Puntos", "PG"],
        ascending=False
    )

    df.reset_index(drop=True, inplace=True)

    return df