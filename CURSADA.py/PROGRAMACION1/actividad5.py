#Ejercicio 5: Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000 por cada estadía como base, se pide el ingreso 
# de una estación del año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del Plata/Córdoba) 
# para vacacionar para poder calcular el precio final:
#-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un descuento del 10% Mar del Plata tiene un descuento del 20%
#-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene un aumento del 10% Mar del Plata tiene un aumento del 20%
#-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el precio sin descuento.
#Validar el ingreso de datos

estacion_del_año = input("Elige la estación del año en la cual desear viajar ")
while(estacion_del_año != "Invierno" and estacion_del_año != "Otoño" and estacion_del_año != "Verano" and estacion_del_año != "Primavera"):
    estacion_del_año = input("Por favor ingresa una estacion del año valida ")

localidad = input("Elegi cual es tu lugar de destino ")
while(localidad != "Bariloche" and localidad != "Cataratas" and localidad != "Mar del Plata" and localidad != "Cordoba"):
    localidad = input("Por favo elegi otro lugar de destino ")

tarifa_inicial = 15000

match(estacion_del_año):
    case "Verano":
        match(localidad):
            case "Bariloche":
                print(f"La estacion y localidad elegida tiene un descuento del 20%, te quedaria la estadia {tarifa_inicial * 0.80} pesos ")
            case  "Cataratas" | "Cordoba":
                print(f"La estacion y localidad elegida tiene un aumento del 10%, te quedaria la estadia {tarifa_inicial * 1.10} pesos")
            case "Mar del Plata":
                print(f"La localidad y estacion elegida tiene un aumento del 20%, te quedaria la estadia {tarifa_inicial * 1.20} pesos")
    case "Invierno":
        match(localidad):
            case "Bariloche":
                print(f"La estacion y localidad elegida tiene un aumento del 20$, te quedaria la estadia {tarifa_inicial * 1.20} pesos ")
            case "Cataratas" | "Cordoba":
                print(f"La estacion y localidad elegida tiene un descuento del 10%, te quedaria la estadia {tarifa_inicial * 0.90} pesos")
            case "Mar del Plata":
                print(f"La estacion y localidad elegida tiene un descuento del 20%, te quedaria la estadia {tarifa_inicial * 0.80} pesos")
    case "Primavera" | "Otoño":
        match(localidad):
            case "Bariloche" | "Cataratas"| "Mar del plata":
                print(f"La estacion y localidad elegida tiene un aumento del 10%, te quedaria la estadia {tarifa_inicial * 1.10} pesos")
            case _:
                print(f"El valor para viajar te queda sin descuento es decir de {tarifa_inicial} pesos")
           
            








