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
from services.taza_service import obtener_tazas

#from models.disco import Disco
#from models.remera import Remera
#from models.taza import Taza



app = Flask(__name__)

@app.route("/")
def inicio():

    discos = obtener_discos()
    remeras = obtener_remeras()
    tazas = obtener_tazas()

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



@app.route("/eliminar/<int:id>")
def eliminar(id):

    eliminar_disco(id)

    return redirect("/dashboard")
    


@app.route("/comprar-disco/<int:id>")
def comprar_disco_route(id):

    comprar_disco(id)

    return redirect("/") 


    
@app.route("/ejemplo")
def ejemplo():
    return render_template("ejemplo.html")

