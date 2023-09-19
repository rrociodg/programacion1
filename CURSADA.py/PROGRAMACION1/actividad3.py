# Ejercicio 3:
# Ingresar 5 números enteros, distintos de cero.  Informar:
# a. Cantidad de pares e impares.
# b. El menor número ingresado.
# c. De los pares el mayor número ingresado.
# d. Suma de los positivos.
# e. Producto de los negativos.

lista_numeros =  []
contador = 0
contador_pares = 0
contador_impares = 0
minimo = None
maximo_pares = None 
suma_positivo = 0
producto_negativo = 1
flag_negativos = False 
flag_pares = False 

for i in range(5):
    numeros= input("Indicame 5 numeros aleatorios ")
    numeros=int(numeros)
    while(numeros == 0):
        numeros= input("Error tienen que ser numeros distintos a 0 ")
        numeros= int(numeros)
    lista_numeros.append(numeros)
#A
    if(numeros % 2 == 0):
        contador_pares += 1
    else:
        contador_impares += 1
#B
    if(minimo == None or numeros < minimo):
        minimo = numeros
#C
    if(numeros % 2 ==0):
        if(maximo_pares == None or numeros > maximo_pares):
            maximo_pares = numeros
            flag_pares = True 
#D
    if numeros > 0:
        suma_positivo += numeros
#E
    if numeros < 0:
        producto_negativo *= numeros
        flag_negativos = True 



mensaje_1 = (f"Hay {contador_pares} numeros pares y {contador_impares} numeros impares")
mensaje_2= (f"El numero minimo ingresado es {minimo}")
if flag_pares == True:
    mensaje_3= (f"El número par maximo es {maximo_pares}")
else:
    mensaje_3= "No se encontraron numeros pares"
mensaje_4=(f"La suma de los numeros positivos es {suma_positivo}")
if flag_negativos == True:
    mensaje_5= (f"El producto de los numeros negativos es de {producto_negativo}")
else:
    mensaje_5="No se ingresaron numeros negativos"

print(mensaje_1)
print(mensaje_2)
print(mensaje_3)
print(mensaje_4)
print(mensaje_5)