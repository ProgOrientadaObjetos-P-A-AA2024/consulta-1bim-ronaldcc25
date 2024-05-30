class Paquetes:

    def __init__(self, p1, p2, p3):
        self.paquete1 = p1
        self.paquete2 = p2
        self.paquete3 = p3

    def paquete1(self, value):
        self.paquete1 = value

    def paquete2(self, value):
        self.paquete2 = value
    
    def paquete3(self, value):
        self.paquete3 = value

    def paquete1(self):
        return self.paquete1

    def paquete2(self):
        return self.paquete2

    def paquete3(self):
        return self.paquete3

    def __str__(self):
        cadena = (f"CONTENIDO PAQUETE 1: {self.paquete1}\nCONTENIDO PAQUETE 2: {self.paquete2}\nCONTENIDO PAQUETE 3: {self.paquete3}")
        return cadena
    
barco = Paquetes("Banano", "Cacao", "Flores")

print(barco)