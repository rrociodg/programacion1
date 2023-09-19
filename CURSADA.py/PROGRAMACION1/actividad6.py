#Ejercicio 6: Utilizar For
# Dada la siguiente lista: [82, 3, 49, 38, 94, 85, 97, 92, 654, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58] mostrar el mayor.

lista_numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 567, 45, 12, 55, 48, 78, 29, 58]
numero_mayor = None 

for numero in lista_numeros:
    if numero_mayor == None or numero > numero_mayor:
        numero_mayor = numero
print(f"El numero maximo de la lista es {numero_mayor}")

# Otra manera de solucionarlo es: LEN(RECORRE LOS ELEMENTOS DE LA LISTA)
lista_numeros = [82, 3, 49, 38, 94, 8585, 97, 92, 654, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
numero_mayor = lista_numeros[0]

for indice in range(len(lista_numeros)):
    if lista_numeros[indice] > numero_mayor:
        numero_mayor = lista_numeros[indice]
print(numero_mayor)

