# Pedir una edad. Informar si la persona es mayor de edad (más de 18 años), adolescente (entre 13 y 17 años) o niño (menor a 13 años).

edad = input("Indicarme tu edad ")
while(not edad.isdigit or int(edad) < 1):
    edad= input("Indicar una edad correcta ")

edad=int(edad)

if edad < 13:
    print(f"Tu edad es de {edad} años, eso significa que eres un niño")
elif edad >= 13 and edad <= 17:
    print(f"Tu edad es de {edad} años, eso significa que sos un adolescente")
else:
    print(f"Tu edad es de {edad} años, sos mayor de edad")
