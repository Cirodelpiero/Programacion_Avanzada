import json

def obtener_tazas():

    with open("database/tazas.json", "r") as archivo:

        tazas = json.load(archivo)

    return tazas


def buscar_taza(id):

    tazas = obtener_tazas()

    for taza in tazas:

        if taza["id"] == id:

            return taza

    return None