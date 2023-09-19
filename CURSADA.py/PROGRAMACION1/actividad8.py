#Ejercicio 8: Dada la siguiente lista: [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58] mostrar el número repetido

lista_numeros = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
repetido = []
unico = []

for i in lista_numeros:
    if i not in unico:
        unico.append(i)
    else:
        if i not in repetido:
            repetido.append(i)
print(f"El numero repetido es {repetido}")