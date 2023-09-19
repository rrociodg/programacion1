#Ejercicio 7: Dada la siguiente lista: [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58] mostrar solo los números pares.

lista_numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58, 10]
numeros_pares = []

for numeros in lista_numeros:
    if (numeros % 2 == 0):
        numeros_pares += [numeros]
print(f"Los numeros pares son {numeros_pares}")
