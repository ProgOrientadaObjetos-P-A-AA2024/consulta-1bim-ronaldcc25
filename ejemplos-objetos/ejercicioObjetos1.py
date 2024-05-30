class Computadora:

    def __init__(self, m, p):
        self.marca = m
        self.precio = p

    def marca(self, m):
        self.marca = m

    def precio(self, p):
        self.precio = p

    def precio(self):
        return self.precio

    def marca(self):
        return self.marca

    def __str__(self):
        cadena = (f"Marca de la Computadora: {self.marca}\nPrecio de la Computadora: {self.precio}")
        return cadena

# Objeto
computadora1 = Computadora("ASUS", 1500)

print(computadora1)