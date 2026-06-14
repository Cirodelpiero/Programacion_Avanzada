import json
from models.remera import Remera


def obtener_remeras():

    with open("database/remeras.json", "r") as archivo:

        remeras = json.load(archivo)

    for remera in remeras:

        producto = Remera(
            id=remera["id"],
            nombre=remera["nombre"],
            precio=remera["precio"],
            stock=remera["stock"],
            banda=remera["banda"],
            imagen_principal=remera["imagen_principal"],
            talle=remera["talle"]
        )

        remera["stock_bajo_alerta"] = producto.stock_bajo()
        remera["agotado"] = producto.agotado()

    return remeras



def buscar_remera(id):

    remeras = obtener_remeras()

    for remera in remeras:

        if remera["id"] == id:
            return remera



def eliminar_remera(id):

    remeras = obtener_remeras()

    remeras_filtradas = []

    for remera in remeras:

        if remera["id"] != id:

            remeras_filtradas.append(remera)

    with open("database/remeras.json", "w") as archivo:

        json.dump(
            remeras_filtradas,
            archivo,
            indent=4
        )

def crear_remera(nueva_remera):

    remeras = obtener_remeras()

    remeras.append(nueva_remera)

    with open("database/remeras.json", "w") as archivo:

        json.dump(
            remeras,
            archivo,
            indent=4
        )  

def generar_id_remera():

    remeras = obtener_remeras()

    if len(remeras) == 0:

        return 1

    ultimo = remeras[-1]

    return ultimo["id"] + 1

      


def editar_remera(remera_editada):

    remeras = obtener_remeras()

    for i in range(len(remeras)):

        if remeras[i]["id"] == remera_editada["id"]:

            remeras[i] = remera_editada


    with open("database/remeras.json", "w") as archivo:

        json.dump(
            remeras,
            archivo,
            indent=4
        )

def guardar_remeras(remeras):

    with open("database/remeras.json", "w") as archivo:

        json.dump(
            remeras,
            archivo,
            indent=4
        )

def comprar_remera(id):
    remeras = obtener_remeras()

    for remera in remeras:
        if remera["id"] == id:

            producto = Remera(
                id=remera["id"],
                nombre=remera["nombre"],
                precio=remera["precio"],
                stock=remera["stock"],
                banda=remera["banda"],
                imagen_principal=remera["imagen_principal"],
                talle=remera["talle"]
            )
            producto.vender_unidad()
            remera["stock"] = producto.stock
            break

    guardar_remeras(remeras)