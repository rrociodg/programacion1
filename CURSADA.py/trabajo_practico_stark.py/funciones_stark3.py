from data_stark import lista_personajes
"""ROCIO NATALI DE GRAZIA 39514625 """
def stark_normalizar_datos(lista_personajes:list)->bool:
    """recorre la lista y normaliza los valores numericos en el 
       caso de que no se haya hecho antes"""

    if not lista_personajes:
        print("La lista de superheroes se encuentra vacia")
        return False
    
    cambios_hechos = False 

    for superheroe in lista_personajes:
        for clave, valor in superheroe.items():
            if clave in ["fuerza", "altura", "peso"]:
                if clave == "fuerza" and type(valor) != int :
                    superheroe[clave] = int(valor)
                    cambios_hechos = True 
                elif clave in ["peso", "altura"] and type(valor) != float:
                    superheroe[clave] = float(valor) 
                    cambios_hechos = True 

    if cambios_hechos:
        print("Datos Normalizados")
        return True 
    else:
        print("Hubo un error al normalizar los datos o los mismos ya fueron normalizados")
        return False

def obtener_dato(diccionario:dict, clave:str)-> bool:
    """brinda el valor de la clave solicitada en el diccionario, se chequea que
    el dict no este vacio y que el valor nombre este incluido dentro de las claves"""

    if not diccionario or "nombre" not in diccionario:
        return False 
    
    if clave in diccionario:
        valor = diccionario[clave]
        print(f"{clave}: {valor}")
        return valor 
    else:
        return False


def obtener_nombre (diccionario:dict)->str:
    """obtiene el valor asociado a la clave 'nombre'
    y lo formatea en un string con un formato "Nombre: Nombre del superheroe" 
    chequea que el dict no este vacio"""

    chequear_nombre = obtener_dato(diccionario, "nombre")
    if chequear_nombre is not False:
        nombre_formateado = (f" Nombre: {chequear_nombre}")
        return nombre_formateado
    else:
        print("Error")
        return False 


def obtener_nombre_y_dato(diccionario:dict, clave:str)->str:
    """Obtiene el nombre y el dato (clave) del héroe y lo formatea en un string con formato 'Nombre: nombre | Clave: dato'
        chequea que el dict no este vacio"""
    nombre = obtener_nombre(diccionario)
    
    if nombre is not False:
        dato = obtener_dato(diccionario, clave)
    
        if dato is not False:
            dato_formateado = (f"Nombre: {nombre} | {clave}: {dato}")
            # print(dato_formateado)
            return dato_formateado
        else:
            return False
    else:
        return False


def obtener_maximo(lista:list, clave:str)->bool:
    """obtiene el valor maximo de la clave elegida en una lista de dict. Chequea que la lista este con datos
    y que el valor que se elija sea int o float, en el caso que no cumpla con estas dos condiciones devuelve False"""
    if not lista:
        print("La lista de superheroes se encuentra vacia")
        return False
    maximo_valor = None      
    for superheroe in lista:
        if clave in superheroe:
            if type(superheroe[clave]) == int or type(superheroe[clave]) == float:
                if maximo_valor == None or superheroe[clave] > maximo_valor:
                    maximo_valor = superheroe[clave]

    # print( f"El valor maximo de {clave} es de {maximo_valor}")                
    return maximo_valor


def obtener_minimo(lista:list, clave:str)->bool:
    """obtiene el valor minimo de la clave elegida en una lista de dict. Chequea que la lista no este vacia 
    y que el dato elegido sea un int o un float, si es asi devuelve False"""

    if not lista:
        print("La lista se encuentra vacia")
        return False 

    minimo_valor = None

    for superheroe in lista:
        if clave in superheroe:
            if type(superheroe[clave]) == int or type(superheroe[clave]) == float:
                if minimo_valor == None or superheroe[clave] < minimo_valor:
                    minimo_valor = superheroe[clave]

    # print(f"El valor minimo para {clave} es {minimo_valor}")                
    return minimo_valor
def obtener_dato_cantidad(lista:list, dato:int or float or str, clave:str)->list:
    """Esta función retorna una lista de héroes que cumplen con la condición de tener el valor 'dato' en la clave 'clave'."""
    resultado_datos = []

    if isinstance(dato, (int, float)):
        for superheroe in lista:
            if superheroe[clave] == dato:
                resultado_datos.append(superheroe)
                # print(f"Coincidencia encontrada para {superheroe['nombre']} con {clave} igual a {dato}")
    else:
        for superheroe in lista:
            if superheroe[clave] == dato:
                resultado_datos.append(superheroe)
                # print(f"Coincidencia encontrada para {superheroe['nombre']} con {clave} igual a {dato}")
    return resultado_datos

def stark_imprimir_heroes(lista_personajes:list)->bool:
    """Imprime la informacion completa de los superheroes que se encuentran en la lista. Valida que la lista no este vacia,
     si es asi retorna False """
    
    if not lista_personajes:
        return False 
    
    for superheroe in lista_personajes:
        print("+-" + "-" * 28 + "-+")
        print("| {:^29} |".format(superheroe.get("nombre", "Desconocido")))
        print("| {:^29} |".format("Identidad: " + str(superheroe.get("identidad", "Desconocido"))))
        print("| {:^29} |".format("Empresa: " + str(superheroe.get("empresa", "Desconocido"))))
        print("| {:^29} |".format("Altura: " + str(superheroe.get("altura", "Desconocido"))))
        print("| {:^29} |".format("Peso: " + str(superheroe.get("peso", "Desconocido"))))
        print("| {:^29} |".format("Género: " + str(superheroe.get("genero", "Desconocido"))))
        print("| {:^29} |".format("Color de ojos: " + str(superheroe.get("color_ojos", "Desconocido"))))
        print("| {:^29} |".format("Color de pelo: " + str(superheroe.get("color_pelo", "Desconocido"))))
        print("| {:^29} |".format("Fuerza: " + str(superheroe.get("fuerza", "Desconocido"))))
        print("| {:^29} |".format("Inteligencia: " + str(superheroe.get("inteligencia", "Desconocido"))))
        print("+-" + "-" * 28 + "-+")
        print() #linea en blanco para separar heroes 
    return True 


def sumar_dato_heroe(lista:list,clave:str)->int or float:
    """Valida que el superheroe sea tipo dict y no este vacio antes de hacer la suma. Suma el valor
    de la clave en todos los superheroes de la lista. Retorna la suma total de los valores"""

    suma_total = 0
    for superheroe in lista:
        if isinstance(superheroe, dict) and clave in superheroe:
            valor = superheroe.get(clave)
            if isinstance(valor, (int, float)):
                suma_total = suma_total + valor 
    # print(f"La suma total de '{clave}' es de {suma_total}")
    return suma_total

def dividir(dividendo:int, divisor:int)->int or float:
    """ Recibe dos numeros como parametros, los divide y retorna el resultado. Si el divisor es 0 retornara False"""
    if divisor == 0:
        print("No se puede dividir por 0")
        return False
    else:
        resultado_division = float(dividendo) / divisor
        # print(f"el resultado de dividir {dividendo} con {divisor} da {resultado_division}")
        return resultado_division

def calculador_promedio(lista:list, clave:str)-> int or float:
    """ Esta funcion primero suma todos los valores validos de la clave especificada en la lista de personajes
    usando la funciom sumar_dato_heroe. Luego calcula el promedio de los datos obtenidos y retorna el resultado"""

    suma_heroe = sumar_dato_heroe(lista, clave)
    cantidad_heroe = 0

    for superheroe in lista:
        if type(superheroe) == dict and clave in superheroe:
            valor = superheroe.get(clave)
            if type(valor) in (int, float):
                cantidad_heroe += 1
    
    if cantidad_heroe == 0:
        return False 
    promedio = dividir(suma_heroe, cantidad_heroe)
    
    # print(f"La cantidad de heroes es de {cantidad_heroe} y el promedio de {clave} de todos ellos da como resultado {promedio}")
    return promedio


def mostrar_promedio_dato(lista:list, clave:str)-> float or bool:
    """Recibe una lista de héroes y una cadena que representa la clave del dato que se desea promediar. Valida que la lista no este
    vacia y que los valores sean int o float, en el caso de que si, retorna False."""

    if not lista:
        print("La lista se encuentra vacia o la clave elegida no puede promediarse")
        return False 

    suma_valor = 0
    acumulador = 0

    for superheroe in lista:
        if clave in superheroe: 
            valor = superheroe[clave]
            if isinstance(valor, (int, float)):
                suma_valor += valor
                acumulador += 1

    if acumulador == 0:
        # print("No se puede promediar si no hay datos numeros en la clave")
        return False 

    else:
        promedio = suma_valor / acumulador
        # print(f"El promedio de {clave} es de {promedio}")    
    return promedio 

def imprimir_menu():
    """Muestra por consola las opciones el cual permite usar las funciones ya programadas anteriormente """
    
    print("BIENVENIDO A INDUSTRIAS STARK \n", 
            "1) Normalizar datos \n", 
            "2) Obtener dato. \n",
            "3) Obtener nombre con formato 'Nombre: Nombre'  \n", 
            "4) obtener nombre y dato con formato'Nombre: nombre | Clave: dato. \n",
            "5) Obtener maximo de la clave. \n",
            "6) Obtener minimo de la clave. \n",
            "7) Obtener dato/cantidad. \n",
            "8) Imprimir datos de los heroes. \n",
            "9) Suma el total de los datos de heroes. \n",
            "10) Dividir \n",
            "11) Calcular el promedio del dato elegido. \n",
            "12) Muestra el promedio del dato elegido. \n",
            "13) Salir \n"
            "-------------------------------------------------------------------------------")
def validar_entero(numero:int)->bool:
    """La funcion verifica si los valores ingresados por parametros son digitos, en el caso que no, devuelve False """
    if numero.isdigit():
        return True
    else:
        return False 

def stark_menu_principal():
    """Esta funcion muestra el menu de la función anterior y castea el numero de la opcion en un int y en el caso de que
    no sea una opcion correcta retorna false""" 
    while True:
        imprimir_menu()
        eleccion = input("¿A cual quisieras ingresar?: ").strip()

        if validar_entero(eleccion):
            return int(eleccion)
        else:
            print("Opcion no valida. Ingrese solo digitos")
def stark_marvel_app(lista:list):
    """Esta funcion se encargará de la ejecución principal de nuestro programa. Debe informar si se marca una opcion incorrecta
    y vuelve a pedirle el dato al usuario."""
    while True:
        eleccion = stark_menu_principal()

        match(eleccion):
            case 1:
                stark_normalizar_datos(lista)
            case 2:
                personaje = int(input("Ingresa el índice del personaje que deseas consultar: "))
                clave = input("Ingrese la clave del dato que se desea verificar: ")
                obtener_dato(lista_personajes[personaje], clave)
            case 3:
                personaje = int(input("Ingresa el índice del personaje del que quieras averiguar el nombre: "))
                obtener_nombre(lista_personajes[personaje])
            case 4:
                personaje = int(input("Ingresa el índice del personaje que deseas consultar: "))
                clave = input("Ingresa la clave del dato que deseas obtener: ")
                obtener_nombre_y_dato(lista_personajes[personaje], clave)
            case 5:
                clave = input("Ingrese la clave del dato para obtener el maximo: ")
                obtener_maximo(lista_personajes, clave)
            case 6:
                clave = input("Ingresa la clave del dato para obtener el minimo: ")
                obtener_minimo(lista_personajes, clave)
            case 7:
                dato = float(input("Ingresa el valor que deseas buscar: "))
                clave = input("Ingresa la clave del dato que deseas buscar: ")
                obtener_dato_cantidad(lista_personajes, dato, clave)
            case 8: 
                stark_imprimir_heroes(lista_personajes)
            case 9:
                clave = input("Ingresa la clave del dato que deseas sumar: ")
                sumar_dato_heroe(lista_personajes, clave)
            case 10:
                dividendo = float(input("Ingresa el dividendo: "))
                divisor = float(input("Ingresa el divisor: "))
                dividir(dividendo, divisor)
            case 11:
                clave = input("Ingresa la clave del dato para calcular el promedio: ")
                calculador_promedio(lista_personajes, clave)
            case 12:
                clave = input("Ingresa la clave del dato para mostrar el promedio: ")
                mostrar_promedio_dato(lista_personajes, clave)
            case 13:
                print("Adios!")
                return False 
            case _:
                print("Opcion no valida, por favor ingrese el dato correcto: ")

def imprimir_menu_2():

    """Muestra por consola las opciones el cual permite usar las funciones ya programadas anteriormente """
    print("+-" + "-" * 40 + "-+")
    print("Bienvenido a 'Stark Industries'\n",
        "1) Normalizar datos \n",
        "2) Nombres de los superheroes  de genero NB \n",
        "3) Superheroe femenino más alto \n",
        "4) Superheroe masculino más alto \n",
        "5) Superheroe masculino más debil \n",
        "6) Superheroe NB más debil \n",
        "7) Fuerza promedio de los superheroe genero NB \n",
        "8) Cantidad de superheroes que tienen cada tipo de color de ojos \n",
        "9) Cantidad de superheroes que tienen cada tipo de color de pelo  \n",
        "10) Lista de superheroes agrupados por color de ojos \n",
        "11) Lista de superheroes agrupados por inteligencia\n",
        "12) Salir. \n") 
    print("+-" + "-" * 40 + "-+")   

def contar_color_ojos(lista:list)->dict:
    """Recorre la lista brindada para buscar los colores de ojos y contarlos """
    tipos_color_ojos = {}
    for superheroe in lista_personajes:
        color_ojos = superheroe["color_ojos"]

        if color_ojos in tipos_color_ojos:
            tipos_color_ojos[color_ojos] += 1
        else:
            tipos_color_ojos[color_ojos] = 1

    for color, cantidad in tipos_color_ojos.items():
        print(f"Color de ojos: {color.capitalize()} - Cantidad: {cantidad} superheroes")
def contar_color_pelo(lista:list)->dict:
    """Recorre la lista de superheroes para buscar los tipos de color de pelo y contar cuantos tienen el mismo"""
    tipo_color_pelo = {}
    for superheroe in lista_personajes:
        color_pelo = superheroe["color_pelo"]

        if color_pelo in tipo_color_pelo:
            tipo_color_pelo[color_pelo] +=1
        else:
            tipo_color_pelo[color_pelo] = 1

    for color, cantidad in tipo_color_pelo.items():
        print(f"Color de pelo: {color.capitalize()} - Cantidad: {cantidad} superheroes")


def listar_por_color(list)->dict:
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

def listar_por_inteligencia(lista:list)->dict:
    superheroes_agrupados_inteligencia = {}
    for superheroe in lista_personajes:
        inteligencia = superheroe["inteligencia"]

        if inteligencia in superheroes_agrupados_inteligencia:
            superheroes_agrupados_inteligencia[inteligencia].append(superheroe)
        else:
            superheroes_agrupados_inteligencia[inteligencia] = [superheroe]

    for inteligencia, superheroe in superheroes_agrupados_inteligencia.items():
        print(f"-----------------------------------------\n Superhéroes con tipo de inteligencia {inteligencia}:")
        for superheroe in superheroe:
            print(superheroe["nombre"])

def stark_menu_principal_2 ():
    """Esta funcion muestra el menu de la función anterior y castea el numero de la opcion en un int y en el caso de que
    no sea una opcion correcta retorna false""" 
    while True:
        imprimir_menu_2()
        pregunta = input("¿A cual quisieras ingresar?: ").strip()

        if validar_entero(pregunta) and int(pregunta) >= 1 and int(pregunta) <= 12:
            return int(pregunta)
        else:
            print("Opcion no valida. Ingrese solo digitos y que los mismos sean dentro de las opciones disponibles")

def stark_marvel_app_2(lista):
    normalizar_datos = False 
    while True:
        pregunta = stark_menu_principal_2()

        if pregunta == 1:
            stark_normalizar_datos(lista_personajes)
            normalizar_datos = True 
        elif not normalizar_datos:
            print("Debes normalizar los datos para poder acceder a las otras opciones del menu")

        elif pregunta == 2:
            lista_nb = obtener_dato_cantidad(lista_personajes, "NB", "genero")
            if lista_nb:
                print("Estos son los superheroes de genero NB que se encuentran en la lista: ")
                stark_imprimir_heroes(lista_nb)
            else:
                print("No se encontraron superheroes de genero NB")

        elif pregunta == 3:
            lista_femeninos = obtener_dato_cantidad(lista_personajes, "F", "genero")

            if lista_femeninos:
                max_femenino = obtener_maximo(lista_femeninos, "altura")
                lista_mas_alto = obtener_dato_cantidad(lista_femeninos, max_femenino, "altura")
                print("Los datos del superheroe femenino más alto son: ")
                stark_imprimir_heroes(lista_mas_alto)
            else:
                print("No se encontraron superhéroes de género femenino en la lista.")
        
        elif pregunta == 4:
            lista_masculinos = obtener_dato_cantidad(lista_personajes, "M", "genero")

            if lista_masculinos:
                max_masculino = obtener_maximo(lista_masculinos, "altura")
                lista_mas_alto= obtener_dato_cantidad(lista_masculinos, max_masculino, "altura")
                print("Los datos del superheroe masculino más alto son: ")
                stark_imprimir_heroes(lista_mas_alto)
            else:
                print("No se encontraron superhéroes de género masculino en la lista.")

        elif pregunta == 5:
            lista_masculinos = obtener_dato_cantidad(lista_personajes, "M", "genero")

            if lista_masculinos:
                min_masculino = obtener_minimo(lista_masculinos, "fuerza")
                lista_mas_debil = obtener_dato_cantidad(lista_masculinos, min_masculino, "fuerza")
                print("Los datos del superheroe masculino más debil es: ")
                stark_imprimir_heroes(lista_mas_debil)
            else:
                print("No se encontraron superhéroes de género masculino en la lista.")

        elif pregunta == 6:
            lista_nb = obtener_dato_cantidad(lista_personajes, "NB", "genero")

            if lista_nb:
                min_nb = obtener_minimo(lista_nb, "fuerza")
                lista_mas_debil = obtener_dato_cantidad(lista_nb, min_nb, "fuerza")
                print("Los datos del superheroe NB más debil es: ")
                stark_imprimir_heroes(lista_mas_debil)
            else:
                print("No se encontraron superhéroes de género NB en la lista.")

        elif pregunta == 7:
            lista_nb = obtener_dato_cantidad(lista_personajes, "NB", "genero")

            if lista_nb:
                promedio_fuerza = calculador_promedio(lista_nb, "fuerza")
                if promedio_fuerza is not False:
                    print(f"El promedio de fuerza de la lista de superheros del genero NB es de {promedio_fuerza}")
            else:
                print("No se encontraron superhéroes de género NB en la lista.")

        elif pregunta == 8:
            contar_color_ojos(lista_personajes)
        elif pregunta == 9:
            contar_color_pelo(lista_personajes)
        
        elif pregunta == 10:
            listar_por_color(lista_personajes)
        
        elif pregunta == 11:
            listar_por_inteligencia(lista_personajes)

        elif pregunta == 12:
            print("¡ADIOS!")
            break




