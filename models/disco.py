from models.producto import Producto

class Disco(Producto):
    def __init__(self, nombre, precio, stock, banda,imagen_principal, año):
        super().__init__(id, nombre,  precio, stock, banda, imagen_principal)
        self.año = año
        
    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base} - año: {self.año}"
    
#disco1 = Disco("Disco Blood Sugar", 20, 30, "RHCP",1991)
#print(disco1.mostrar_info())  
