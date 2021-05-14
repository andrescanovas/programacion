# ___________CONSULTAR NO DEJA RESPUESTA EN CADA NOMBRE___________

# for i in range (0, 3):
#     nombre = input("ingrese su nombre :").capitalize()
#     anio_nacimiento = int(input("ingrese año de nacimiento :"))

# edad = 2021 - anio_nacimiento

# if(edad >= 18):
#     print(nombre,"ES MAYOR DE EDAD")
# else:
#     print(nombre,'ES MENOR DE EDAD')



#------------------------------------ ALMACENA DATOS forma 1-------------------------

# datos = []
# datos2 = []

# for i in range (0,3):
#     nombre = input("ingrese su nombre :").capitalize()
#     anio_nacimiento = int(input("ingrese año de nacimiento :"))

# edad = 2021 - anio_nacimiento

# datos.append(datos)
# datos.append(datos2)

# if(edad >= 18):
#     print(nombre,"ES MAYOR DE EDAD")
# else:
#      print(nombre,'ES MENOR DE EDAD')

# print(datos)
# print(datos2)


# -----------------------ALMACENA DATOS 2-------------


datos = []

for i in range (0,3):
    nombre = input("ingrese su nombre :").capitalize()
    anio_nacimiento = int(input("ingrese año de nacimiento :"))

    edad = 2021 - anio_nacimiento

    datos.append([nombre, edad])

    if(edad >= 18):
        print(nombre,"ES MAYOR DE EDAD")
    else:
        print(nombre,'ES MENOR DE EDAD')

for persona in datos:
        print(datos)
