#Ejercicio 9: Dadas las siguientes listas:
# edades = [25,36,18,23,45]
# nombre = ["Juan","Ana","Sol","Mario","Sonia"]
# y considerando que la posición en la lista corresponde a la misma persona, mostar el nombre de la persona más joven

lista_edades = [25,36,18,23,45]
lista_nombre = ["Juan","Ana","Sol","Mario","Sonia"]

menor_edad = lista_edades[0]
nombre_minimo = None

for i in range(len(lista_edades)):
    if lista_edades[i] < menor_edad:
        menor_edad = lista_edades[i]
        nombre_minimo = lista_nombre[i]
print(f"La persona mas pequeña tiene {menor_edad} y se llama {nombre_minimo}")