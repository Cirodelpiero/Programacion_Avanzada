class Producto:
    def __init__(self,id, nombre,precio,stock, banda, imagen_principal):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock    
        self.banda = banda
        self.imagen_principal = imagen_principal    


    def mostrar_info(self):
        return f"{self.nombre} - {self.precio} - {self.stock} - {self.banda}"
    
    def actualizar_stock(self,cantidad):
        self.stock += cantidad

    def aplicar_descuento(self,porcentaje):
        self.precio -= self.precio * (porcentaje/100)

    def disponible(self):
        return self.stock > 0    