from data_stark import lista_personajes
import re 
"""DE GRAZIA ROCIO DNI 39514625"""
def extraer_iniciales(heroe:str)->str:
    """ Extrae las iniciales del heroe y lo devuelve en un str con las iniciales del mismo 
    separado por un punto"""

    if not heroe:
        return "N/A"
    heroe = re.sub(r"-", " ", heroe) 
    iniciales = re.findall(r'\b(?!the\b)\w', heroe)  #busca cualquier carácter alfanumérico que no forme parte de la palabra "the"
    if iniciales:
        return ".".join(iniciales) 
    else:
        return "N/A"

def definir_iniciales_nombre(heroe:dict)->bool:
    """Agrega una nueva clave al dict que se llama 'iniciales' y se reutiliza funcion anterior. El dato
    recibido sea del tipo dict y que el dict contenga el nombre clave. Devuelve un booleano """

    if type(heroe) is not dict or "nombre" not in heroe:
        return False 

    iniciales= extraer_iniciales(heroe["nombre"])
    heroe["iniciales"] = iniciales
    return True 

def agregar_iniciales_nombre(lista_heroes:list)-> bool:
    """La funcion valida que la lista se trate de una, que contenga como minimo un elemento, y se agregar el valor 
    de la funcion anterior. En el caso de que no se pueda, la misma retornara False y brindara un msj especifico por
    pantalla. Si funciona todo correcto devolvera True"""

    if type(lista_heroes) is not list or len(lista_heroes) == 0:
        print("‘El origen de datos no contiene el formato correcto’")
        return False 
    
    for heroe in lista_heroes:
        resultado = definir_iniciales_nombre(heroe)
        if resultado is False:
            print("Ocurrio un error")
            return False 
    return True


def stark_imprimir_nombre_con_iniciales(lista_heroes:list):

    """Imprime la lista completa de superheroes con los nombres de los mismos e incluidas sus iniciales entre (). Reutiliza funcion anterior"""
    if type(lista_heroes) is not list or len(lista_heroes) == 0: 
        print("¡Error con la carga de iniciales!")
    else:
        if agregar_iniciales_nombre(lista_heroes):
            for heroe in lista_heroes:
                nombre = heroe["nombre"]
                iniciales = heroe["iniciales"]

                print(f"* {nombre} ({iniciales})")

def generar_codigo_heroe(id_heroe:int, genero_heroe:str) -> str:
    """Genera un codigo de ID con un formato 'GENERO-000...000ID' Valida que sean numeros y que el genero sea 'F,M O NB'"""
    if not re.match(r'^(M|F|NB)$', genero_heroe) or not genero_heroe: #verifica si la cadena genero_heroe es válida según el patrón "M", "F" o "NB"  
        return "N/A"

    match genero_heroe:
        case "NB":
            codigo = f"{genero_heroe}-{str(id_heroe).zfill(7)}"
        case "F"| "M":
            codigo = f"{genero_heroe}-{str(id_heroe).zfill(8)}"
        case _:
            return "N/A"

    return codigo
# generar_codigo_heroe(52, "F")

def agregar_codigo_heroe(heroe:dict, id_heroe:int)->bool:

    if not heroe or not isinstance(heroe, dict):    
        return False 

    codigo = generar_codigo_heroe(id_heroe, heroe["genero"])
    
    heroe['codigo_heroe'] = codigo
    return True 

def stark_generar_codigos_heroes (lista_heroes:list):
    """Le agrega el codigo a cada uno de los personajes, surgen de la posicion del mismo dentro de la lista"""
    contador = 1

    if lista_heroes == []:
        print("El origen de datos no contiene el formato correcto. ")
    else:
        for heroe in lista_heroes:
            if type(heroe) != dict and "genero" in heroe == False:
                print("El origen de datos no contiene el formato correcto. ")
            else:
                codigo_heroe = generar_codigo_heroe(contador, heroe["genero"])
                agregar_codigo_heroe(heroe, codigo_heroe)
                if contador == 1:
                    id_primer_heroe = codigo_heroe
                else:
                    id_ultimo_heroe = codigo_heroe
                contador += 1
                codigos_super = len(lista_heroes)


    print(f"Se asignaron {codigos_super} codigos")
    print(f"*El codigo del primer heroe es {id_primer_heroe}")
    print(f"*El codigo del ultimo heroe es {id_ultimo_heroe}")   
# stark_generar_codigos_heroes (lista_personajes)
def sanitizar_entero(numero_str:str)->int:
    """La funcion analiza el str recibido y analiza si se trata de un entero positivo. Retorna distintos valores segun cual sea el str ingresado. 
    Elimina espacios vacios"""

    numero_str = numero_str.strip()
    entero = re.search("[0-9]+", numero_str)
    
    if not entero:
        return -1 # significa que no tiene numeros enteros 
    numero = int(numero_str)
    if numero < 0:
        return -2  #el numero es negativo 
    elif numero > 0:
        return numero #el numero es entero 
    else:
        return -3   #otro error

def sanitizar_flotante(numero_str:float)->float:
    """La funcion analiza el str recibido y analiza si se trata de un flotante. Retorna distintos valores segun cual sea el str ingresado. 
    Elimina espacios vacio"""

    numero_str = numero_str.strip()
    flotante = re.search("[0-9]", numero_str)

    if not flotante:
        return -1
    numero = float(numero_str)
    if numero < 0:
        return -2  
    elif numero > 0:
        return numero 
    else:
        return -3 

def sanitizar_string(valor_str:str, valor_por_defecto:str = "-")-> str:
    """Analiza el str recibido y verifica que si ex texto, en el caso de ser asi agrega, castea el texto a minusculas. Si hay // se eliminan 
    por espacios. Se crea un parametro opcional. Si hay numeros retorna N/A"""
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()
    valor_str = re.sub("/", " ", valor_str)  

    if re.search("[0-9]+", valor_str):
        return "N/A"
    
    if not valor_str and valor_por_defecto:
        return valor_por_defecto.lower()

    return valor_str.lower()

def sanitizar_dato(heroe:dict, clave:str, tipo_dato: int or float or str)->bool:
    """La función deberá sanitizar el valor del diccionario correspondiente a la clave y al tipo de dato recibido. 
    Es decir verifica que la clave este dentro del dict, que el tipo de dato sea int float o str, caso contrario arroja error."""
    tipo_dato = tipo_dato.lower() 

    if tipo_dato not in("string", "entero", "flotante"):
        print("Tipo dato no reconocido")
        return False 

    if clave not in heroe:
        print("‘La clave especificada no existe en el héroe’")
        return False 


    atributo = heroe[clave]

    if tipo_dato == "string":
        sanitizacion = sanitizar_string(atributo, "-")
    if tipo_dato == "entero":
        sanitizacion = sanitizar_entero(atributo)
    if tipo_dato == "flotante":
        sanitizacion = sanitizar_flotante(atributo)

    heroe[clave] = sanitizacion

    
    return True 

def stark_normalizar_datos(lista_heroes:list):
    """Esta funcion recorre la lista de heroes y sanitiza las claves ‘altura’, ‘peso’, ‘color_ojos’, ‘color_pelo’, ‘fuerza’ e
    ‘inteligencia’ al finalizar brinda un mensaje. Se valida que la lista no este vacia. Se reutiliza una la funcion anterior"""

    if lista_heroes == []:
        print("Error, la lista se encuentra vacia")
    for heroe in lista_heroes:
        sanitizar_dato(heroe, "altura", "flotante")
        sanitizar_dato(heroe, "peso", "flotante")
        sanitizar_dato(heroe, "color_ojos", "string")
        sanitizar_dato(heroe, "color_pelo", "string")
        sanitizar_dato(heroe, "fuerza", "entero")
        sanitizar_dato(heroe, "inteligencia", "string")
        
    print("Datos normalizados")


def generar_indice_nombres(lista_heroes:list):
    """La funcion genera una lista donde cada elemento es cada palabra que compone el nombre de los personajes. Si la lista esta vacia, 
    si no es un dict o si no esta el nombre incluido en el personaje arroajara un error"""
    nombres_compuesto = []
    if lista_heroes == []:
        print("‘El origen de datos no contiene el formato correcto’")
    else:
        for heroe in lista_heroes:
            if type(heroe) != dict and "nombre" in heroe == False:
                print("‘El origen de datos nocontiene el formato correcto’")
            else: 
                nombre = heroe["nombre"]
                nombre_separado = re.split(r'\W+', nombre)  # Dividimos el nombre en sub cadenas  utilizando \W+ como separador \W coincide con lo que no es un numero o una letra 
                nombres_compuesto.extend(nombre_separado)  #  se agrega a la lista 

        return nombres_compuesto
    
def stark_imprimir_indice_nombre(lista_heroes:list):
    """Se muestra por pantalla el indice generado por la funcion anterior con todos los nombres separados por guion"""
    lista_heroes = generar_indice_nombres(lista_heroes)
    separador = "-".join(lista_heroes)
    print(separador)

def convertir_cm_a_mts(valor_cm:float)-> float:
    """La función deberá retornar el número recibido, pero convertido a la unidad metros. En caso de no ser un float postivo retorna -1 """
    if isinstance(valor_cm, (int, float)) and valor_cm >= 0: # para comprobar si un objeto pertenece a una clase o tipo de datos específico.
        valor_metros = valor_cm / 100
        print(valor_metros)
        return valor_metros
    else:
        return -1
    
def generar_separador(patron:str, largo: int or float, imprimir: "bool" = True)-> str:
    """Genera un separador con el patrón especificado repetido tantas veces como el largo dado(sin salto de linea)
    Si imprimir es True, lo imprime por pantalla antes de retornarlo."""

    if len(patron) < 1 or len(patron) > 2:
        return "N/A"
    if type(largo) != int or largo < 1 or largo > 235:
        return "N/A"
    
    separador = patron * largo 

    if imprimir:
        print(separador)
    return separador 

def generar_encabezado(titulo:str)->str:
    """La funcion devuelve un str que contega el titulo entre dos separadores y en mayusculas"""

    separador = "*" * 189
    encabezado = f"{separador}\n {titulo.upper()} \n{separador}"
    print(encabezado)
    return encabezado

def imprimir_ficha_heroe(heroe:dict)->str:
    """Genera un string con los datos del heroe y lo imprime con un formato especifico."""
    nombre = heroe["nombre"]
    iniciales = heroe["iniciales"]
    identidad = heroe["identidad"]
    consultora = heroe["empresa"]
    codigo = heroe["codigo_heroe"]
    altura_metros = convertir_cm_a_mts(heroe["altura"])
    peso = heroe["peso"]
    fuerza = heroe["fuerza"]
    color_pelo = heroe["color_pelo"]
    color_ojos = heroe["color_ojos"]
    inteligencia = heroe["inteligencia"]

    # Generar encabezado "PRINCIPAL"
    generar_encabezado("PRINCIPAL")

    print(f"NOMBRE DEL HÉROE: {nombre} {iniciales}")
    print(f"IDENTIDAD SECRETA: {identidad}")
    print(f"CONSULTORA: {consultora}")
    print(f"CÓDIGO DE HÉROE : {codigo}")

    #Generar encabezado "FISICO"
    generar_encabezado("FISICO")

    print(f"ALTURA: {altura_metros} Mtrs.")
    print(f"PESO: {peso} Kg.")
    print(f"FUERZA: {fuerza}")

    # Generar encabezado "SEÑAS PARTICULARES"
    generar_encabezado("SEÑAS PARTICULARES")

    print(f"COLOR DE OJOS: {color_ojos}")
    print(f"COLOR DE PELO: {color_pelo}") 
    print(f"INTELIGENCIA: {inteligencia}")

def stark_navegar_fichas(lista_heroes:list):
    """ Esta funcion imprime la primer ficha del heroe y luego solicita al usuario que ingrese alguna de las opciones donde 1 es 
    ir a la izquierda, 2 a la derecha y S es salir"""

    indice = 0
    while True:
        imprimir_ficha_heroe(lista_heroes[indice])
        print("\n[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir")
        opcion_previo = input("Ingrese una opcion: ").strip()
        opcion = opcion_previo.upper()

        if opcion == "1":
            indice -= 1
            if indice < 0: # Si el índice es menor que 0. Se ajusta el índice para que apunte al último elemento de la lista.
                indice = len(lista_heroes) - 1
        elif opcion == "2":
            indice += 1
            if indice >= len(lista_heroes): # Si el índice es igual o mayor que la longitud de la lista
                indice = 0   # ajustar el índice para que apunte al primer elemento de la lista.
        elif opcion == "S":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Ingrese una de las 3 opciones disponibles.")
  
def imprimir_menu():
    """La funcion imprime un menu de opciones por pantalla"""
    print("Bienvenido a industrias Stark: \n"
            "1 - Imprimir la lista de nombres junto con sus iniciales \n",
            "2 - Generar códigos de héroes \n",
            "3 - Normalizar datos \n",
            "4 - Imprimir índice de nombres \n",
            "5 - Navegar fichas \n",
            "S - Salir \n",
            "-------------------------------------------------------------------------------")

def stark_menu_principal()-> int or str:
    """La funcion imprime el menu de opciones y le pide al usuario que ingrese a una. Retorna la respuesta del usuario"""
    
    imprimir_menu()
    while True:
        respuesta_= input("Ingrese una opción: ").strip()
        respuesta = respuesta_.upper()

        if respuesta in["1","2","3","4","5","S"]:
            return respuesta
        else:
            print("Opción no válida. Ingrese una opción del 1 al 5 o S para salir.")

def stark_marvel_app(lista_heroes):
    """Se crea la app para que el usuario pueda interactuar entre las funciones """
    codigos_hechos = False
    datos_normalizados = False 
    while True:
        opcion = stark_menu_principal()

        if opcion == "1":
            stark_imprimir_nombre_con_iniciales(lista_heroes)
        elif opcion == "2":
            stark_generar_codigos_heroes(lista_heroes)
            codigos_hechos = True
        elif opcion == "3":
            stark_normalizar_datos(lista_heroes)
            datos_normalizados = True 
        elif opcion == "4":
            stark_imprimir_indice_nombre(lista_heroes)
        elif opcion == "5":
            if datos_normalizados and codigos_hechos:
                    stark_navegar_fichas(lista_heroes)
            else:
                if not codigos_hechos and not datos_normalizados:
                    print("Generar codigos y normalizar datos primero.")
                elif not codigos_hechos:
                    print("\n•No se generaron los codigos, marque primero dicha opción.\n")
                elif not datos_normalizados:
                    print("\n•No se normalizaron los datos, marque primero dicha opción.\n")            
        elif opcion == "S":
            print("¡Adiós!")
            break





