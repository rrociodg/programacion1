import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

class App(customtkinter.CTk):
    
    def _init_(self):
        super()._init_()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.lista_de_nombres = ["Juan", "María", "Pedro", "Laura", "Carlos", "Ana", "Luis", "Elena", "Miguel", "Sofía"]
        self.lista_plato_principal = ["Pizza", "Hamburguesa", "Ensalada", "Pizza","Hamburguesa", "Ensalada", "Pizza", "Hamburguesa", "Ensalada", "Pizza"]
        self.lista_cantidad_de_platos = [2, 1, 3, 2, 2, 4, 3, 1, 1, 3]
        self.lista_bebidas_elegidas = ["Refresco", "Agua", "Jugo", "Refresco","Agua", "Jugo", "Refresco", "Agua", "Jugo", "Refresco"]
        self.lista_cantidad_de_bebidas = [2, 1, 5, 3, 2, 5, 1, 2, 1, 3]

# En el parque de diversiones "Aventuras Extremas", un grupo de amigos ha decidido disfrutar
# del día probando las diferentes atracciones y luego se reúnen en un restaurante para compartir
# un delicioso almuerzo. Antes de que llegue la cuenta, deciden crear un programa para calcular
#y dividir los gastos de manera equitativa. Se pide ingresar los siguientes datos hasta que el
# usuario lo desee:
#Para cada amigo:
#- Nombre del amigo,
#- Plato principal elegido ("Pizza", "Hamburguesa", "Ensalada").
#- Cantidad de platos principales pedidos (debe ser al menos 1).
#- Bebida elegida ("Refresco", "Agua", "Jugo").
#- Cantidad de bebidas pedidas (debe ser al menos 1). 
# Se conocen los siguientes precios base:
#El precio unitario de cada plato principal es de $800.
#El precio unitario de cada bebida es de $200.
#Una vez ingresados todos los datos, el programa debe calcular e informar lo siguiente:



# NOMBRE DEL AMIGO 
for i in range(2):
    nombre= input("¿Cual es tu nombre? ")
    while (nombre == None or not nombre.isalpha()):
        nombre = input("Indicar nombre nuevamente")
    print(f"Tu nombre es {nombre}")

#- Plato principal elegido ("Pizza", "Hamburguesa", "Ensalada").
    plato_principal= input("¿Que te gustaria de plato principal? ")
    while (plato_principal!= "Pizza" and plato_principal!= "Hamburguesa" and plato_principal!= "Ensalada"): 
        plato_principal = input("Elegi una comida del menú")
    print(f"Elegiste para comer {plato_principal}")

#- Cantidad de platos principales pedidos (debe ser al menos 1).
    cantidad_platos = input("¿Cuantos platos vas comer? ")
    while (not cantidad_platos.isdigit() or int(cantidad_platos) <= 0):
        cantidad_platos = input("Por favor, ingresa una cantidad valida")

    print(f"Usted eligio {cantidad_platos} platos para comer")

#- Bebida elegida ("Refresco", "Agua", "Jugo").
    bebida_elegida = input("¿Que deseas tomar? ")
    while (bebida_elegida!= "Refresco" and bebida_elegida!= "Agua" and bebida_elegida!= "Jugo"):
        bebida_elegida = input("Elegir una bebida correcta")

    print(f"Eligio para tomar {bebida_elegida}")

# Cantidad de bebidas pedidas (debe ser al menos 1)
    cantidad_bebidas = input("¿Cuantas bebidas quieres tomar? ")
    while (not cantidad_bebidas.isdigit() or int(cantidad_bebidas) <= 0):
        cantidad_bebidas = input("Elija una cantidad permitida")

    print(f"Eligio para tomar {cantidad_bebidas} bebidas")



# A) El total gastado por el grupo (resultante del costo de los platos principales y las bebidas), y la propina sugerida para el personal del
#  restaurante (esta corresponde al 10% del total gastado).
def btn_mostrar_on_click(self):
    precio_plato = 800
    precio_bebida = 200
    acumulador_platos = 0
    acumulador_bebidas = 0
    total_gastado = 0
    propina = 0

    for i in range(len(self.lista_nombres)):
        acumulador_bebidas += self.lista_cantidad_de_bebidas[indice]
        acumulador_platos += self.lista_cantidad_de_platos[indice]
    total_gastado = (acumulador_bebidas * precio_bebida) + (acumulador_platos * precio_plato)
    propina = total_gastado * 100 / 10
    print(f"El total que se gasto es de {total_gastado} pesos, y se dejo de propina {propina}")

#B) Promedio del dinero gastado en “Jugo”, sobre el grupo de amigos en general.

#C) Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad). #Ejemplo: [30% pizza, 40% ensaladas, 30% hamburguesas]
#D) Además, desean premiar al amigo que realizó la mayor CANTIDAD de pedidos en total (platos principales + bebidas) con una entrada gratuita para otra atracción del parque"Aventuras Extremas".
