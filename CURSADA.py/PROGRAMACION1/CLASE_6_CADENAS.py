# Un objeto va a tener minimamente dos cosas
# 1. propiedades 
# 2.metodos (funciones asociadas a esa variable- funciones propias de los objetos, y se llaman metodos y estan dentro de la variable

# La variable es un objeto! objeto de clase str
# ej: persona es algo abstracto
# TEXTO = "HOLA MUNDO"
# Todo lo que este en comillas simples o dobles, es una cadena, las cadenas son de tipo INMUTABLE, si se cambia es porque se asigna un nuevo valor 
# texto = "Hola mundo" 
# print(type(texto))

"""
Un metodo es una funcion especial, que existe para un dato en particular. Para trabajar con cadenas de texto en python, se emplea una serie de me
                                                todos a las variables de tipo STR

METODOS:
variable = "Hola mundo" 

*variable.strip(): El metodo strip eliminara todos los caracteres vacios que pueda contener la variable, de izquierda o derecha en el medio NO. (a los de la propia variable que contiene el metodo)
*variable.lower(): El metodo convierte las letras en minusculas de la variable que contiene el metodo, sirve para normalizar los datos
*variable.upper(): pasa todo a mayusculas 
*cadena.capitalize(): la primera mayuscula despues minuscula

*cadena.replace(): reemplaza un cojunto de caracteres por otro
    EJ:  cadena = "Hola mundo"
         cadena = cadena.replace("la","@")
         cadena = "Ho@ mundo"

*cadena.split(","): divide una cadena en subcadenas y las devuelve almacenadas en una lista 
    EJ: cadena = "Python,Java,C"
        print(cadena.split(","))
        ["Python", "Java", "C"]

*cadena.join(): es la contra de split devuelve la primera cadena unida a cada uno de los elementos de la lista que se le pasa como parametro 
    EJ:  cadena = "-"
        cadena = cadena.join(["A", "B", "C"])
        print(cadena) # A-B-C

*cadena.zfill():rellena la cadena con ceros a la izquierda hasta la longitud pasada como parametro
    EJ:     cadena = "314"
            print(cadena.zfill(6))
            #000314

Para validar(todos los que empiecen con IS-bool):
*cadena.isalpha(): Devuelve un booleano. Devuelve True si todos los caracteres son alfabeticos, False de lo contrario. Tiene que ser SOLO ALFABETICOS
tampoco espacios 
*cadena.isalnum(): Devuelve un booleano. Cadena que solo puede contener letras y numeros. Si tiene espacios False. 

*cadena.count(): permite contar las veces que otra cadena se encuentra dentro de la primera. Un len optimizado para buscar cosas especificas
    EJ:     cadena = "Hola Mundo Hola"
            print(cadena.count("la")) # 2

*cadena.format(): son reemplazadas con los valores de las variables pasadas
*(len(cadena)): longitud de la cadena de texto
                cadena = "Hola Mundo"
                print(len(cadena)) # 10
*Slice: cadena[desde:hasta]: el primer numero es donde comienza y el segundo numero de indice es donde termina 

    EJ:     cadena = "Hola Mundo"
            print(cadena[5:10]) # Mundo
            print(cadena[5:]) # Mundo
            print(cadena[:5]) # Hola
"""




