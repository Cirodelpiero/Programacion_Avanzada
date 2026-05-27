from models.producto import Producto

class Disco(Producto):

    def __init__(
        self,
        id,
        nombre,
        precio,
        stock,
        banda,
        imagen_principal,
        anio
    ):

        super().__init__(
            id,
            nombre,
            precio,
            stock
        )

        self.banda = banda
        self.imagen_principal = imagen_principal
        self.anio = anio