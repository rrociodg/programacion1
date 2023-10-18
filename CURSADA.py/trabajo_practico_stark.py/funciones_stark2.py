from data_stark import lista_personajes
from collections import Counter

def superheroes_nb(lista_personajes): #A
    '''imprime por consola el nombre de cada superhéroe de género NB'''
    flag = False
    for superheroe in lista_personajes:
        if superheroe["genero"] == "NB":
            print(superheroe["nombre"])
            flag = True
    if not flag:
        print("No hay ningún personaje de genero no binario")
        print("-----------------------------------------------")


def superheroe_femenina_alta(lista_personajes): #B
    '''muestra el superheroe femenino más alto'''
    altura_maxima = None
    for superheroe in lista_personajes:
        if(superheroe["genero"] == "F"):
            altura_actual = float(superheroe["altura"]) 
            if(altura_maxima == None or altura_actual > altura_maxima):
                altura_maxima = altura_actual
                nombre_femenina_alta = superheroe["nombre"]
    print(f"La superheroe femenina mas alta es {nombre_femenina_alta} con una altura de {altura_maxima} cm.")
    print("------------------------------------------------------------------------------------------------")
    

def superheroe_masculino_alto(lista_personajes): #C
    '''nombre masculino mas alto'''
    altura_maxima = None
    for superheroe in lista_personajes:
        if(superheroe["genero"] == "M"):
            altura_actual = float(superheroe["altura"])
            if(altura_maxima == None or altura_actual > altura_maxima):
                altura_maxima = altura_actual
                nombre_masculino_alto = superheroe["nombre"]
    print(f"El superheroe masculino más alto es {nombre_masculino_alto} con una altura de {altura_maxima} cm.")
    print("--------------------------------------------------------------------------------------------------")
    

def superheroe_masculino_mas_debil(lista_personajes): #D
    '''personaje masculino más debil'''
    debil_maximo = None
    for superheroe in lista_personajes:
        if(superheroe["genero"] == "M"):
            actual_debil = float(superheroe["fuerza"])
            if(debil_maximo == None or actual_debil < debil_maximo):
                debil_maximo = actual_debil
                nombre_masculino_debil = superheroe["nombre"]
    print(f"El superheroe masculino mas debil es {nombre_masculino_debil} con una fuerza de {debil_maximo}")
    print("------------------------------------------------------------------------------------------------")

def superheroe_no_binario_mas_debil(lista_personajes): #E
    '''buscar el superheroe no binario más debil'''
    debil_maximo_nb = None
    for superheroe in lista_personajes:
        if(superheroe["genero"] == "NB"):
            debil_maximo_actual = float(superheroe["fuerza"])
            if(debil_maximo_nb == None or debil_maximo_nb > debil_maximo_actual):
                debil_maximo_nb = debil_maximo_actual
                nombre_debil_nb = superheroe["nombre"]

    if nombre_debil_nb:
        print(f"La persona más debil del genero NB es {nombre_debil_nb} con una fuerza de {debil_maximo_nb}")
    else:
        print("No se encuentra ningun personaje de genero NB para poder indicar la fuerza del mas debil")
    print("------------------------------------------------------------------------------------------------")


def fuerza_promedio_superheroes_nb(lista_personajes):  #F
    '''calcula el promedio de la fuerza del genero NB'''
    contador_nb = 0
    acumulador_fuerza_nb = 0
    for superheroe in lista_personajes:
        if(superheroe["genero"] == "NB"):
            acumulador_fuerza_nb += float(superheroe["fuerza"])
            contador_nb += 1
    if contador_nb != 0:
        promedio_fuerza = acumulador_fuerza_nb / contador_nb
        mensaje = print(f"El promedio de fuerza de los personajes de genero NB es de {promedio_fuerza}")
    else:
        mensaje = print("No hay personajes NB para sacar un promedio")
    print("------------------------------------------------------------------------------------------------")
            
def tipo_ojos_superheroes(lista_personajes): #G
    '''recorre la lista para buscar los colores de ojos'''
    tipos_color_ojos = {}
    for superheroe in lista_personajes:
        color_ojos = superheroe["color_ojos"]

        if color_ojos in tipos_color_ojos:
            tipos_color_ojos[color_ojos] += 1
        else:
            tipos_color_ojos[color_ojos] = 1
    for color, cantidad in tipos_color_ojos.items():
        print(f"Color de ojos: {color.capitalize()} - Cantidad: {cantidad} superheroes")

def tipo_color_pelo(lista_personajes): #H
    '''Tipo de color de cabello'''
    conteo_colores_de_pelo = {} # ALMACENA LOS COLORES DE PELO 

    for superheroe in lista_personajes:
        color = superheroe["color_pelo"]

        if color in conteo_colores_de_pelo:
            conteo_colores_de_pelo[color] += 1 # SI EL COLOR ya esta se incrementa uno 
        else:
            conteo_colores_de_pelo[color] = 1 # si no esta se crea 

    for color, cantidad in conteo_colores_de_pelo.items():
        print(f"Hay {cantidad} superheroes con pelo color {color}.")
       
def grupo_color_de_ojos(lista_personajes): #I
    """recorre la lista para brindar agrupados los superheroes por color de ojos"""
    superheroes_agrupados_color = {}
    for superheroe in lista_personajes:
        color_ojos = superheroe["color_ojos"]
        
        if color_ojos in superheroes_agrupados_color:
            superheroes_agrupados_color[color_ojos].append(superheroe)
        else:
            superheroes_agrupados_color[color_ojos] = [superheroe]

    for color, superheroe in superheroes_agrupados_color.items():
        print(f"----------------------------------- \n Superhéroes con color de ojos {color.capitalize()}: ")
        for superheroe in superheroe:
            print(superheroe["nombre"])


def lista_nivel_inteligencia(lista_personajes): #J
    '''Lista de los superheroes por inteligencia'''
    nivel_inteligencia = {}

    for superheroe in lista_personajes:
        inteligencia = superheroe.get("inteligencia", "")
        nombre_super = superheroe["nombre"]

        if inteligencia in nivel_inteligencia:
            nivel_inteligencia[inteligencia].append(nombre_super) 
        else:
            nivel_inteligencia[inteligencia] = [nombre_super]

    for inteligencia, lista_personajes in nivel_inteligencia.items():
        print(f"Nivel de inteligencia: {inteligencia}")
        for nombre_super in lista_personajes:
            print(f"{nombre_super}")
        print()
        print("-----------------------------------------------------")



# def grupo_color_de_ojos(lista_personajes): #I
#     '''Lista de superheroes por color de ojos'''
#     ojos_superheroe = {}

#     for superheroe in lista_personajes:
#         color_de_ojos = superheroe["color_ojos"]
#         nombre_super = superheroe["nombre"]

#         if color_de_ojos in ojos_superheroe:
#             ojos_superheroe[color_de_ojos].append(nombre_super)
#         else:
#             ojos_superheroe[color_de_ojos] = [nombre_super]
#         print(f"{nombre_super} tiene ojos de color {color_de_ojos}")
#     return ojos_superheroe