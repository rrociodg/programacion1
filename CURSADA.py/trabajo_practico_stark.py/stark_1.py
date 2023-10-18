from data_stark import lista_personajes
"""ALMUNO: ROCIO NATALI DE GRAZIA DNI 39514625""" 

superheroes_fuerza_maxima = []
fuerza_maxima = None
altura_heroe_mas_bajo = None

contador_femenino = 0
fuerza_femenino = 0

flag = True 
while(flag):
    print("¿A cual opción le gustaria ingresar?: \n",
        "A) Ver los atributos de todos los superheroes  \n",
        "B) Identidad y peso del superheroe con mayor fuerza \n",
        "C) Nombre e identidad del superheroe más bajo \n",
        "D) Peso promedio de los superheroes masculinos \n",
        "E) Nombre y peso de los superheroes con mayor fuerza que el promedio de fuerza de genero femenino \n "
        "F) Salir \n")
    respuesta = input("Ingrese su respuesta: ")        
    match(respuesta):
        case "A":
            for personajes in lista_personajes:
                print("Nombre:", personajes["nombre"]) 
                print("Identidad:", personajes["identidad"])
                print("Empresa:", personajes["empresa"])
                print("Altura:", personajes["altura"])
                print("Peso:", personajes["peso"])
                print("Género:", personajes["genero"])
                print("Color de ojos:", personajes["color_ojos"])
                print("Color de pelo:", personajes["color_pelo"])
                print("Fuerza:", personajes["fuerza"])
                print("Inteligencia:", personajes["inteligencia"])
                print("-------------------------------")

        case "B":
            for personajes in lista_personajes:
                personaje_actual = int(personajes["fuerza"])
                if(fuerza_maxima == None or personaje_actual > fuerza_maxima):
                    fuerza_maxima = personaje_actual
                    superheroes_fuerza_maxima = [personajes]
                elif personaje_actual == fuerza_maxima:
                    superheroes_fuerza_maxima.append(personajes)


            if superheroes_fuerza_maxima:
                for personajes in superheroes_fuerza_maxima:
                    identidad_mas_fuerte = personajes["identidad"]
                    peso_mas_fuerte = personajes["peso"]
                    print(f"El superheroe más fuerte se llama {identidad_mas_fuerte} con un peso de : {peso_mas_fuerte} kg, y una fuerza de : {fuerza_maxima}")

        case "C":
            for personajes in lista_personajes:
                personaje_actual = float(personajes["altura"])
                if(altura_heroe_mas_bajo == None or personaje_actual < altura_heroe_mas_bajo):
                    altura_heroe_mas_bajo = personaje_actual
                    nombre_heroe_mas_bajo = personajes["nombre"]
                    identidad_hero_mas_bajo = personajes["identidad"]
            print(f"El nombre del personaje más bajo es {nombre_heroe_mas_bajo}, su identidad es {identidad_hero_mas_bajo} y su altura es de {altura_heroe_mas_bajo}")

        case "D":
            contador_masculino = 0
            acumulador_peso = 0 
            for personajes in lista_personajes:
                if(personajes["genero"] == "M"):
                    acumulador_peso += float(personajes["peso"])
                    contador_masculino += 1

            promedio_peso = acumulador_peso / contador_masculino
            print(f"El peso promedio de los superheroes masculinos es de {promedio_peso}")

        case "E":
            for personajes in lista_personajes:
                if(personajes["genero"] == "F"):
                    fuerza_femenino += float(personajes["fuerza"])
                    contador_femenino += 1
        
            promedio_fuerza = fuerza_femenino / contador_femenino

            print(f"El promedio de fuerza de genero femino es de {promedio_fuerza}")  

            for personajes in lista_personajes:
                if(float(personajes["fuerza"]) > promedio_fuerza):
                    nombre_fuerte = personajes["nombre"]
                    fuerza_fuerte = personajes["fuerza"]
                    peso_mas_fuerte = personajes["peso"]
                    print(f"{nombre_fuerte} tiene más fuerza que la fuerza promedio femenina: {fuerza_fuerte}, y tiene un peso de {peso_mas_fuerte} kg")
        case "F":
            flag = False 
        
        case _:
            print("Ingrese una opción valida")

  


                              

    

