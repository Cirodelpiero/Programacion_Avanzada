from flask import Flask, render_template, request, redirect
from flask import redirect
from services.disco_service import obtener_discos
from services.disco_service import buscar_disco
from services.disco_service import eliminar_disco
from services.disco_service import crear_disco
from services.disco_service import generar_id
from services.disco_service import editar_disco
from services.disco_service import comprar_disco


from services.remera_service import obtener_remeras
from services.remera_service import crear_remera 
from services.remera_service import generar_id_remera
from services.remera_service import buscar_remera
from services.remera_service import editar_remera
from services.remera_service import eliminar_remera


from services.taza_service import obtener_tazas
from services.taza_service import buscar_taza

#from models.disco import Disco
#from models.remera import Remera
#from models.taza import Taza



app = Flask(__name__)

@app.route("/")
def inicio():

    discos = obtener_discos()
    remeras = obtener_remeras()
    tazas = obtener_tazas()
    tazas = [] 

    return render_template(
        "index.html",
        discos=discos,
        remeras = remeras,
        tazas = tazas
        
    )



@app.route("/dashboard")
def dashboard():
    discos = obtener_discos()
    remeras = obtener_remeras()

    print("ENTRO AL DASHBOARD")
    

    return render_template("dashboard.html", discos=discos, remeras=remeras)


@app.route("/disco/<int:id>")
def ver_disco(id):

    disco = buscar_disco(id)

    return render_template(
        "detalle_disco.html", disco=disco)

@app.route("/taza/<int:id>")
def ver_taza(id):

    taza = buscar_taza(id)

    return render_template(
        "detalle_taza.html", taza=taza)


@app.route("/crear", methods=["GET", "POST"])
def crear():

    if request.method == "POST":

        nombre = request.form["nombre"]

        precio = int(request.form["precio"])

        stock = int(request.form["stock"])

        banda = request.form["banda"]

        imagen_principal = request.files["imagen_principal"]

        imagen_principal.save(
            "static/img/" + imagen_principal.filename
        )

        anio = int(request.form["anio"])


        nuevo_disco = {

            "id": generar_id(),

            "nombre": nombre,

            "precio": precio,

            "stock": stock,

            "banda": banda,

            "imagen_principal": imagen_principal.filename,

            "anio": anio
        }


        crear_disco(nuevo_disco)

        return redirect("/dashboard")


    return render_template("crear.html")

@app.route("/crear_remera", methods=["GET", "POST"])
def crear_remera_route():

    if request.method == "POST":

        nombre = request.form["nombre"]

        precio = int(request.form["precio"])

        stock = int(request.form["stock"])

        banda = request.form["banda"]

        imagen_principal = request.files["imagen_principal"]

        imagen_principal.save(
            "static/img/imgRemeras/" + imagen_principal.filename
        )

        talle = request.form["talle"]


        nueva_remera = {

            "id": generar_id_remera(),

            "nombre": nombre,

            "precio": precio,

            "stock": stock,

            "banda": banda,

            "imagen_principal": imagen_principal.filename,

            "talle": talle
        }


        crear_remera(nueva_remera)

        return redirect("/dashboard")


    return render_template("crear_remera.html")


@app.route("/remera/<int:id>")
def ver_remera(id):
    remera = buscar_remera(id)
    return render_template("detalle_remera.html", remera=remera)



@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    disco = buscar_disco(id)

    if request.method == "POST":

        disco["nombre"] = request.form["nombre"]

        disco["precio"] = int(request.form["precio"])

        disco["stock"] = int(request.form["stock"])

        disco["banda"] = request.form["banda"]

        disco["anio"] = int(request.form["anio"])


        imagen_principal = request.files["imagen_principal"]


        if imagen_principal.filename != "":

            imagen_principal.save(
                "static/img/" + imagen_principal.filename
            )

            disco["imagen_principal"] = imagen_principal.filename


        editar_disco(disco)

        return redirect("/dashboard")


    return render_template(
        "editar.html",
        disco=disco
    )


@app.route("/editar_remera/<int:id>", methods=["GET", "POST"])
def editar_remera_route(id):
    remera = buscar_remera(id)

    if request.method == "POST":
        remera["nombre"] = request.form["nombre"]
        remera["precio"] = int(request.form["precio"])
        remera["stock"] = int(request.form["stock"])
        remera["banda"] = request.form["banda"]
        remera["talle"] = request.form["talle"]

        imagen_principal = request.files["imagen_principal"]

        if imagen_principal.filename != "":
            imagen_principal.save("static/img/imgRemeras/" + imagen_principal.filename)
            remera["imagen_principal"] = imagen_principal.filename

        editar_remera(remera)
        return redirect("/dashboard")

    return render_template("editar_remera.html", remera=remera)



@app.route("/eliminar/<int:id>")
def eliminar(id):

    eliminar_disco(id)

    return redirect("/dashboard")
    

@app.route("/eliminar_remera/<int:id>")
def eliminar_remera_route(id):
    eliminar_remera(id)
    return redirect("/dashboard")


@app.route("/comprar-disco/<int:id>")
def comprar_disco_route(id):

    comprar_disco(id)

    return redirect("/") 



@app.route("/comprar-remera/<int:id>")
def comprar_remera_route(id):
    from services.remera_service import comprar_remera
    comprar_remera(id)
    return redirect(f"/remera/{id}")

 
    
@app.route("/ejemplo")
def ejemplo():
    return render_template("ejemplo.html")


if __name__ == "__main__":
    app.run(debug=True)