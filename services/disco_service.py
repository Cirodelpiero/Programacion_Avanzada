import json
from models.disco import Disco


def obtener_discos():

    with open("database/discos.json", "r") as archivo:
        discos = json.load(archivo)

    for disco in discos:

        producto = Disco(
            id=disco["id"],
            nombre=disco["nombre"],
            precio=disco["precio"],
            stock=disco["stock"],
            banda=disco["banda"],
            imagen_principal=disco["imagen_principal"],
            anio=disco["anio"]
        )

        disco["stock_bajo_alerta"] = producto.stock_bajo()

    return discos



def buscar_disco(id):

    discos = obtener_discos()

    for disco in discos:

        if disco["id"] == id:
            return disco



def eliminar_disco(id):

    discos = obtener_discos()

    discos_filtrados = []

    for disco in discos:

        if disco["id"] != id:

            discos_filtrados.append(disco)

    with open("database/discos.json", "w") as archivo:

        json.dump(
            discos_filtrados,
            archivo,
            indent=4
        )

def crear_disco(nuevo_disco):

    discos = obtener_discos()

    discos.append(nuevo_disco)

    with open("database/discos.json", "w") as archivo:

        json.dump(
            discos,
            archivo,
            indent=4
        )  

def generar_id():

    discos = obtener_discos()

    if len(discos) == 0:

        return 1

    ultimo = discos[-1]

    return ultimo["id"] + 1

      


def editar_disco(disco_editado):

    discos = obtener_discos()

    for i in range(len(discos)):

        if discos[i]["id"] == disco_editado["id"]:

            discos[i] = disco_editado


    with open("database/discos.json", "w") as archivo:

        json.dump(
            discos,
            archivo,
            indent=4
        )
def guardar_discos(discos):

    with open("database/discos.json", "w") as archivo:

        json.dump(
            discos,
            archivo,
            indent=4
        )

def comprar_disco(id):
    discos = obtener_discos()

    for disco in discos:
        if disco["id"] == id:

            
            producto = Disco(
                id=disco["id"],
                nombre=disco["nombre"],
                precio=disco["precio"],
                stock=disco["stock"],
                banda=disco["banda"],
                imagen_principal=disco["imagen_principal"],
                anio=disco["anio"]
)
            producto.vender_unidad()
            disco["stock"] = producto.stock
            break

    guardar_discos(discos)