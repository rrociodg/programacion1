# #Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su sueldo para esa persona.

nombre= input("¿Cual es tu nombre? ")
while (nombre== None or not nombre.isalpha()):
    nombre = input("Ingresar su nombre ")

sueldo= input("Indicarme tu sueldo ")
sueldo=float(sueldo)
while(float(sueldo)<= 0):
    sueldo = input("Indicar tu sueldo ")
    sueldo = float(sueldo)

aumento = sueldo * 10 / 100 
incremento = sueldo + aumento 

#  #  tambien se puede hacer sueldo = sueldo + sueldo * 0.1

print(f"Tu nombre es {nombre}, y tu sueldo actualmente es de {sueldo}, con un incremento del 10% te quedaria un sueldo de {incremento} pesos")
