anio_naciemieto = int(input("ingrese año de nacimiento:"))
anio_actual = int(input("ingrese fechaactual:"))
edadminima = int(input("ingrese la edad minima:"))


Edad_de_postulantes = anio_actual - anio_naciemieto 

if(Edad_de_postulantes >= edadminima):
    print("aprobado")
else:
    print("rechazado")

print("fin") 