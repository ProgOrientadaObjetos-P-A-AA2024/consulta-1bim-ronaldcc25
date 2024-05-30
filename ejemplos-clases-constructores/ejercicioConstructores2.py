class Colegio():
    
    # Constructor
    def __init__(self, estudiante, notas, materia):
        self.estudiante = estudiante
        self.materia = materia
        self.notaFinal = notas

    def estudiante(self, e):
        self.estudiante = e
    
    def materia(self, m):
        self.materia = m
    
    def notaFinal(self, n):
        self.notaFinal = n

    def estudiante(self):
        return self.estudiante

    def materia(self):
        return self.materia

    def notaFinal(self):
        return self.notaFinal
    
    def __str__(self):
        cadena = (f"\nNombre del Estudiante: {self.estudiante}\nNombre de la Materia: {self.materia}\nNota final de la Materia: {self.notaFinal}")
        return cadena
    
nombre = input("Ingrese el nombre del Estudiante: ")
materia = input("Ingrese el nombre de la materia: ")
notaFinal = input(f"Nota final del Estudiante {nombre} en la Materia de {materia}: ")

estudiante1 = Colegio(nombre, notaFinal, materia)
print(estudiante1)