
#Ejercicio 10: Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus respectivas listas. Validar el ingreso de datos según su criterio.
#Datos: nombre, sexo (f/m), nota (validar).
# Una vez cargados los datos:
# Mostrar el nombre del hombre con nota más baja
# Mostrar el promedio de notas de las mujeres
# Ejemplo:
# nombres = ["Juan","Pedro","Sol","Paco","Ana"]
# sexo = ["m","m","f","m","f"]
# nota = [6,8,10,8,5]
# print(f"Los numeros que elegiste son {lista_numeros}")

nombres = ["Juan","Pedro","Sol","Paco","Ana"]
genero = ["m","m","f","m","f"]
nota = [6,8,10,8,5]

for i in range(5):
    nombres= input("¿Cual es tu nombre? ")
    while (nombres == None or not nombres.isalpha()):
        nombres = input("Indicar nombre nuevamente")
    nombres.append(nombres)

    genero= input("Ingresa tu genero")
    while(genero != "f" and genero != "m"):
        genero= input("Ingresa tu genero")
    genero.append(genero)

    nota= input("Indica la nota")
    while(nota == None or not nota.isdigit()):
        nota = input("Ingresa solo digitos")
    nota.append(nota)
