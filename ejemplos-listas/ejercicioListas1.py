class Notas():
    
    nota = []
    tamanio = int(input("Ingrese el tamaño para la lista: "))

    for i in range(tamanio):
        dato = int(input(f"Ingrese una nota en la posicion {i}: "))
        nota.append(dato)

    print(f"\nLa lista final es: {nota}")