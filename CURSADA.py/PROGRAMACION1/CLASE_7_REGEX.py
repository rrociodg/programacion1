import re 

""" EXPRESIONES REGURALES:
Son una serie de simbolos que nos permitirian definir patrones de busqueda en cadenas de textos. 

Se debe importar el termino re: "import re".  Cuenta con un conjunto de metodos que permiten comprobar si una determinada cadena coincide 
con una expresion regular dada. """

# SPLIT:Retorna una lista que contiene la cadena dividida por el número de ocurrencias del patrón.

print(re.split(" ", "Hola Mundo"))
print(re.split("[a-z ]", "hola 1chicas")) # """Quita las letras de A a Z"""
print(re.split("[a-zA-Z1-9 ]", "hola@ 15454chicas")) #"""Quita las letras de A a Z tanto mayuscula como minuscula y los numeros del 1 al 9"""

# SEARCH: Retorna re.Match object si contiene por lo menos una ocurrencia del patrón y None si no encuentra ninguna. El desde es INCLUSIVO 
# el hasta es excluyente. Me dice si esta o no la expresion buscada 
 
print(re.search(" ", "texto"))
"""El + se indica cuando se quiere mostrar una o mas ocurrencias, el {} es para poner como minimo """
print(re.search("[0-9]+ ", "el texto 123 ingresado"))
print(re.search(" ", "el texto").span())
print(re.search(" ", "el texto").start())
""" Donde empieza la coincidencia"""
print(re.search("[a-z]", "el texto").end())
""" Donde termina la coincidencia"""

# FINDALL: Retorna una lista que contiene todas las coincidencias del pattern («patrón»). El findall al contratrio de split, va a buscar dentro de 
# la cadena todas las ocurrencias de la expresion que le este pasando. El split lo sacaba. Si no hay coincidencia devuelve un conjunto vacio

texto = ' uno 1 dos 25 tres 3 cuatro'

print(re.findall(" ", texto))

print(re.findall("[0-9]", texto))
"""Busca los numeros del cero al 9"""
print(re.findall("[0-9]+", texto))
""" Se agrega el más si hay más coincidencias"""
print(re.findall("[a-z]", texto))
"""Busca de a-z"""
print(re.findall("[a-z]+", texto))
"""Busca de a-z pero si hay coincidencias juntas lo toma por el elemento"""
print(re.findall("[a-z]{4}+", texto))
"""Lo busca por limite pedido"""

# SUB: Reemplaza una o más coincidencias

texto = "abc ccc ddd abc aaa"

resultado = re.sub("abc", "", texto)
print(resultado)
"""Elimina lo pedido en el segundo parametro"""

resultado = re.sub("abc", "hola@", texto)
print(resultado)
"""Reemplaza lo pedido en el primer parametro por el segundo"""

resultado = re.sub(r"\s+", "-", texto)  #reemplazará todos los espacios en blanco con guiones
print(resultado)
"""Elimina los espacios duplicados, y si en el segundo parametro se le indica un valor se reemplaza el valor vacio por ese elemento"""

# TEXTO 

texto = "NATHY PELUSO || BZRP Music Sessions # 36"

# Nathy peluso y Music sessions: SON TEXTO CUALQUIERA- son los textos buscados
# Doble barra y numeral: SEPARADORES
# NUMERO: Un numero cualquiera

# print(re.split(" [||]+ " , texto))
# print(re.split(" \|\| " , texto))
# print(re.split(" \|+ ", texto)) 
# print(re.split(" \|{2} ", texto))

# print(re.split(" \|+ | # ", texto))
# print(re.split(" [\| #]+ ", texto))
# print(re.split("([a-zA-Z ]+)\|\|([a-zA-Z]+)#([0-9]+)", texto))


fecha = "2022-02-03 19:23:45"

print(re.split(" ", fecha))
print(re.split(" [0-9]{2}:[0-9]{2}:[0-9]{2}", fecha))

print(re.findall("[0-9]{2,4}",fecha))
print(re.findall("[0-9]{4}",fecha)) #solo año 
print(re.findall("-([0-9]{2})-",fecha)) #solo mes
print(re.findall("-([0-9]{2}) ",fecha)) #solo dia
print(re.findall("[0-9]{2,4}-[0-9]{2}-[0-9]{2}", fecha))

año = "([0-9]{2,4})"
mes = "([0-9]{1,2})"
dia = "([0-9]{1,2})"

print(re.findall(f"{año}-{mes}-{dia}", fecha))


""" SINTAXIS 
[] : Conjunto de caracteres "[a-z]" 
\  : Permite determinar secuencias especiales y escapar caracteres \d
.  : Hace referencia a cualquier caracter "ho.a"
^  : Empieza con "^hola"
$  : termina con "mundo$"
*  : ninguna o mas ocurrencias "ho.*a"
+  : una o mas ocurrencias "ho.+a"
?  : cero o una ocurrencia "ho.?a"
{} : especifica el numero de ocurrencias "ho.{1}a"
|  : una o la otra "hola|chau"
() : permite seleccionar un grupo """