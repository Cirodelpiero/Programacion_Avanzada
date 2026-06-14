from models.producto import Producto

class Remera(Producto):
    def __init__(self, id, nombre, precio, stock, banda, imagen_principal, talle):
        # Al padre (Producto) SOLO le mandamos sus 4 datos básicos
        super().__init__(id, nombre, precio, stock)
        
        # El resto los guarda la Remera por su cuenta
        self.banda = banda
        self.imagen_principal = imagen_principal
        self.talle = talle

    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base} - Talle: {self.talle}"