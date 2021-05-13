temperatura_lunes = int(input("ingrese la temperatura del dia lunes"))
temperatura_martes = int(input("ingrese la temperatura del dia martes"))
temperatura_miercoles = int(input("ingrese la temperatura del dia miercoles"))
temperatura_jueves = int(input("ingrese la temperatura del dia jueves"))
temperatura_viernes = int(input("ingrese la temperatura del dia viernes"))
temperatura_sabado = int(input("ingrese la temperatura del dia sabado"))
temperatura_domingo = int(input("ingrese la temperatura del dia domingo"))

presion_lunes = int(input("ingrese la presion del dia lunes"))
presion_martes = int(input("ingrese la presion del dia martes"))
presion_miercoles = int(input("ingrese la presion del dia miercoles"))
presion_jueves = int(input("ingrese la presion del dia jueves"))
presion_viernes = int(input("ingrese la presion del dia viernes"))
presion_sabado = int(input("ingrese la presion del dia sabado"))
presion_domingo = int(input("ingrese la presion del dia domingo"))


promedio_de_temperatura = (temperatura_lunes + temperatura_martes + temperatura_miercoles + temperatura_jueves + temperatura_viernes + temperatura_sabado + temperatura_domingo) / 7

promedio_de_presion = (presion_lunes + presion_martes + presion_miercoles + presion_jueves + presion_viernes + presion_sabado + presion_domingo) / 7

print("El promedio de temperatura de la semana es: ", promedio_de_temperatura , "El promedio de presion de la semana es: ", promedio_de_presion)