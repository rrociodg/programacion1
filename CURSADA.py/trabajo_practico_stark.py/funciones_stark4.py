from data_stark import lista_personajes
import re 

def extraer_iniciales(heroe:str)->str:
    """ Extrae las iniciales del heroe y lo devuelve en un str con las iniciales del mismo 
    separado por un punto"""

    if not heroe:
        return "N/A"
    heroe = re.sub(r"-", " ", heroe) #se utiliza para reemplazar los guiones por un espacio 
    iniciales = re.findall(r'\b(?!the\b)\w', heroe) #se utiliza para sacar el THE, en el caso de no estar seguro con si las letras estan en minuscula o mayuscula se puede usar re.IGNORECASE
    if iniciales:
        return ".".join(iniciales) #los une por puntos
    else:
        return "N/A"
# print(extraer_iniciales("Pepe Grillo"))

def definir_iniciales_nombre(heroe:dict)->bool:
    """Agrega una nueva clave al dict que se llama 'iniciales' y se reutiliza funcion anterior. El dato
    recibido sea del tipo dict y que el dict contenga el nombre clave. Devuelve un booleano """

    if type(heroe) is not dict or "nombre" not in heroe:
        return False 

    iniciales= extraer_iniciales(heroe["nombre"])
    heroe["iniciales"] = iniciales
    return True 

# nombre = {"nombre": "Mystique", "identidad": "Raven Darkholme", "empresa": "Marvel Comics", "altura": "178.65000000000001"}
# definir_iniciales_nombre(nombre)

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
# print(agregar_iniciales_nombre(lista_personajes))

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
stark_imprimir_nombre_con_iniciales(lista_personajes)

def generar_codigo_heroe(id_heroe:int, genero_heroe:str) -> str:
    """Genera un codigo de ID con un formato 'GENERO-000...000ID' Valida que sean numeros y que el genero sea 'F,M O NB'"""
    if type(id_heroe) is not int or id_heroe < 0:
        return "N/A"

    if not re.match(r'^(M|F|NB)$', genero_heroe) or not genero_heroe:
        return "N/A"

    codigo = f"{genero_heroe}- {str(id_heroe).zfill(9)}"
    print(codigo)
    return codigo
# generar_codigo_heroe(5432587,"F")

def agregar_codigo_heroe(heroe:dict, id_heroe:int)->bool:

    if type(heroe) is not dict:
        return False
 
    genero_heroe = heroe["genero"]
    codigo = generar_codigo_heroe(id_heroe, genero_heroe)

    if len(codigo) == 10:
        heroe["codigo_heroe"] = codigo 
        return True
    else:
        return False
# agregar_codigo_heroe({"nombre": "Spider-Man", "genero": "M"}, 45820)

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
                id_heroe = generar_codigo_heroe(contador, heroe["genero"])
                agregar_codigo_heroe(heroe, id_heroe)
                if contador == 1:
                    id_primer_heroe = id_heroe
                else:
                    id_ultimo_heroe = id_heroe
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
        return -2 #el numero es negativo 
    elif numero > 0:
        return numero #el numero es entero 
    else:
        return -3 #otro error
# print(sanitizar_entero("5"))

def sanitizar_flotante(numero_str:float)->float:
    """La funcion analiza el str recibido y analiza si se trata de un flotante. Retorna distintos valores segun cual sea el str ingresado. 
    Elimina espacios vacio"""

    numero_str = numero_str.strip()
    flotante = re.search("[0-9]", numero_str)

    if not flotante:
        return -1 #no tiene numeros 
    numero = float(numero_str)
    if numero < 0:
        return -2 #numero negativo 
    elif numero > 0:
        return numero #lo devuelve en float
    else:
        return -3 #otro error 
# print(sanitizar_flotante("5.25"))

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

# resultado1 = sanitizar_string("Texto sin números")
# resultado2 = sanitizar_string("123 Texto con números")
# resultado3 = sanitizar_string("Texto con /// barra")
# resultado4 = sanitizar_string("", "ValorPorDefecto")
# resultado5 = sanitizar_string("  Texto con espacios en blanco  ")

# print(resultado1)  # Salida: "texto sin números"
# print(resultado2)  # Salida: "N/A"
# print(resultado3)  # Salida: "texto con   barra"
# print(resultado4)  # Salida: "valorpordefecto"
# print(resultado5)  # Salida: "texto con espacios en blanco"

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
    
    return True 

heroe = {
    "nombre": "Spider-Man",
    "edad": "25",
    "altura": "1.75",
    "genero": "M"}

# resultado1 = sanitizar_dato(heroe, "edad", "entero")
# print(f"Resultado 1: {resultado1}")

def stark_normalizar_datos(lista_heroes:list):
    """Esta funcion recorre la lista de heroes y sanitiza las claves ‘altura’, ‘peso’, ‘color_ojos’, ‘color_pelo’, ‘fuerza’ e
    ‘inteligencia’ al finalizar brinda un mensaje. Se valida que la lista no este vacia. Se reutiliza una la funcion anterior"""

    if lista_heroes == []:
        print("Error, la lista se encuentra vacia")
    claves_sanitizar = ['altura', 'peso', 'color_ojos', 'color_pelo', 'fuerza', 'inteligencia']

    for heroe in lista_heroes:
        for clave in claves_sanitizar:
            if clave in heroe:
                sanitizar_dato(heroe, clave, "string")
    print("Datos normalizados")
# stark_normalizar_datos(lista_personajes)

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
                nombre_separado = re.split(r'\W+', nombre) # Dividimos el nombre en palabras utilizando \W+ como separador
                nombres_compuesto.extend(nombre_separado)

        return nombres_compuesto
# print(generar_indice_nombres(lista_personajes))

def stark_imprimir_indice_nombre(lista_heroes:list):
    """Se muestra por pantalla el indice generado por la funcion anterior con todos los nombres separados por guion"""
    lista_heroes = generar_indice_nombres(lista_heroes)
    separador = "-".join(lista_heroes)
    print(separador)
# stark_imprimir_indice_nombre(lista_personajes)

def convertir_cm_a_mts(valor_cm:float)-> float:
    """La función deberá retornar el número recibido, pero convertido a la unidad metros. En caso de no ser un float postivo retorna -1 """
    if isinstance(valor_cm, (int, float)) and valor_cm >= 0:
        valor_metros = valor_cm / 100
        print(valor_metros)
        return valor_metros
    else:
        return -1
# convertir_cm_a_mts(18.449999999999999)

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
# print(generar_separador("*", 25))
def generar_encabezado(titulo:str)->str:
    """La funcion devuelve un str que contega el titulo entre dos separadores y en mayusculas"""

    separador = "*" * 189
    encabezado = f"{separador}\n {titulo.upper()} \n{separador}"
    print(encabezado)
    return encabezado
# generar_encabezado("hola")

def imprimir_ficha_heroe(heroe:dict)->str:
    """Genera un string con los datos del heroe y lo imprime con un formato especifico."""

    nombre = heroe["nombre"]
    iniciales = heroe["iniciales"]
    identidad = heroe["identidad"]
    consultora = heroe["empresa"]
    # codigo = heroe["codigo_heroe"]
    altura = convertir_cm_a_mts(heroe["altura"])
    peso = heroe["peso"]
    fuerza = heroe["fuerza"]
    color_pelo = heroe["color_pelo"]
    color_ojos = heroe["color_ojos"]

    encabezado_principal = generar_encabezado("PRINCIPAL")
    print(f"NOMBRE DEL HÉROE: {nombre} {iniciales}")
    print(f"IDENTIDAD SECRETA: {identidad}")
    print(f"CONSULTORA: {consultora}")
    # print(f"CÓDIGO DE HÉROE : {codigo}")
    encabezado_fisico = generar_encabezado("FISICO")
    print(f"ALTURA: {altura} Mtrs.")
    print(f"PESO: {peso} Kg.")
    print(f"FUERZA: {fuerza}")
    encabezado_señas_particulares = generar_encabezado("SEÑAS PARTICULARES")
    print(f"COLOR DE OJOS: {color_ojos}")
    print(f"COLOR DE PELO: {color_pelo}") 

def stark_navegar_fichas(lista_heroes:list):
    """ Esta funcion imprime la primer ficha del heroe y luego solicita al usuario que ingrese alguna de las opciones donde 1 es 
    ir a la izquierda, 2 a la derecha y S es salir"""
    indice_actual = 0
    while True:
        imprimir_ficha_heroe(lista_heroes[indice_actual])
        print("\n[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir")
        opcion_previo = input("Ingrese una opcion: ").strip()
        opcion = opcion_previo.upper()
        if opcion == "1":
            indice_actual -= 1
        if indice_actual < 0:
            indice_actual = len(lista_heroes) - 1
        elif opcion == "2":
            indice_actual += 1
            if indice_actual >= len(lista_heroes):
                indice_actual = 0
        elif opcion == "S":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Ingrese una de las 3 opciones disponibles.")
stark_navegar_fichas(lista_personajes)

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
# imprimir_menu()

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
     while True:
        opcion = stark_menu_principal()

        if opcion == "1":
            stark_imprimir_nombre_con_iniciales(lista_heroes)
        elif opcion == "2":
            stark_generar_codigos_heroes(lista_heroes)
        elif opcion == "3":
            stark_normalizar_datos(lista_heroes)
        elif opcion == "4":
            stark_imprimir_indice_nombre(lista_heroes)
        elif opcion == "5":
            stark_navegar_fichas(lista_heroes)
        elif opcion == "S":
            print("¡Adiós!")
            break
        else:
            print("Opción incorrecta. Por favor, seleccione una opción válida.")
# stark_marvel_app(lista_personajes)


    

