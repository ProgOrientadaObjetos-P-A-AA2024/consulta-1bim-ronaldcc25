# Inicializamos el diccionario de coordenadas 
coordenadas = {}

while True:
    punto = input("Ingrese el nombre del punto (o 'fin' para terminar): ")
    if punto.lower() == 'fin':
        break
    x = float(input("Ingrese la coordenada x: "))
    y = float(input("Ingrese la coordenada y: "))
    
    # Almacenar las coordenadas en un diccionario usando una tupla como clave
    coordenadas[(x, y)] = punto

# Mostrar el diccionario completo de coordenadas
print("Diccionario de coordenadas:")
for coordenada, punto in coordenadas.items():
    print(f"{punto}: ({coordenada[0]}, {coordenada[1]})")
