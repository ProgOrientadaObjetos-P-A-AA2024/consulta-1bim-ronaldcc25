class Auto():

    # Constructor
    def __init__(self, marca, modelo, anioFabricacion):    
        self.marca = marca    
        self.modelo = modelo
        self.anio = anioFabricacion
    
    # Establecer Marca
    def marca(self, m):
        self.marca = m

    # Establecer Modelo
    def modelo(self, mod):
        self.modelo = mod
    
    # Establecer Año
    def anio(self, a):
        self.anio = a

    # Obtener Marca
    def marca(self):
        return self.marca
    
    # Obtener Modelo
    def modelo(self):
        return self.modelo

    # Obtener Año
    def anioFabricacion(self):
        return self.anio
    
    def __str__(self):
        cadena = (f"\nMARCA DEL AUTO: {marca}\nMODELO DEL AUTO: {modelo}\nAÑO DE FABRICACION: {anioFabricacion}")
        return cadena
        

marca = input("Ingrese la marca del auto: ")
modelo = input("Ingrese el modelo del auto: ")
anioFabricacion = int(input("Ingrese el año de fabricacion del auto: "))

cliente1 = Auto(marca, modelo, anioFabricacion)

print(cliente1)
