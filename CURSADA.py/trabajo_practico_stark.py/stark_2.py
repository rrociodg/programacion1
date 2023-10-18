from data_stark import lista_personajes
from funciones_stark2 import *

# Usando como base lo realizado en el anterior desafío realizar los siguientes
# informes en un menú
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género NB
# B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
# género NB
# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# I. Listar todos los superhéroes agrupados por color de ojos.
# J. Listar todos los superhéroes agrupados por tipo de inteligencia
# NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú


flag = True 
while(flag):
    print("Bienvenido a 'Stark Industries' elija la opcion que desea: \n",
        "A) Nombre del superheroe genero no binario \n",
        "B) Superheroe femenina más alta \n",
        "C) Superheroe masculino más alto \n",
        "D) Superheroe masculino más debil \n",
        "E) Superheroe no binario más debil \n",
        "F) Fuerza promedio de los superheroes no binarios \n",
        "G) Tipo de color de ojos \n",
        "H) Tipo de color de cabello \n",
        "I) Lista de superheroes por color de ojos \n",
        "J) Lista de superheroes por tipo de inteligencia \n",
        "K) Salir del menú \n") 
    respuesta = input("Ingrese su respuesta: ")        
    match(respuesta):
        case "A":
            superheroes_nb(lista_personajes)
        case "B":
            superheroe_femenina_alta(lista_personajes)
        case "C":
            superheroe_masculino_alto(lista_personajes)
        case "D":
            superheroe_masculino_mas_debil(lista_personajes)
        case "E":
            superheroe_no_binario_mas_debil(lista_personajes)
        case "F":
            fuerza_promedio_superheroes_nb(lista_personajes)
        case "G": 
            tipo_ojos_superheroes(lista_personajes)
        case "H":
            tipo_color_pelo(lista_personajes)
        case "I":
            grupo_color_de_ojos(lista_personajes)
        case "J":
            lista_nivel_inteligencia(lista_personajes)
        case "K":
            flag = False 
        case _:
            print("Por favor indicar una opción correcta")


   