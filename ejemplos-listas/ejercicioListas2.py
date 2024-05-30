class Suma:

    arreglo = [1, 2, 4, 8, 14]

    suma = 0

    for i in arreglo: 
        suma += i
    
sumaArreglo = Suma()
print(f"La suma del arreglo es: {sumaArreglo.suma}")