# Ejercicio 4: Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO ser soltero.

edad = input("¿Cual es tu edad? ")
edad = int(edad)

estado_civil = input("¿Tu estado civil es Soltero o En pareja? ")
while (estado_civil != "Soltero" and estado_civil != "En pareja"):
    estado_civil = input("Por favor ingrese una opción valida ")

if (edad < 18 and estado_civil != "Soltero"):
    print(f"Tu edad es de {edad} años y eso significa que eres muy pequeño para NO ser soltero")

else:
    print(f"Tu edad es {edad} años y es correcta para tener pareja")
