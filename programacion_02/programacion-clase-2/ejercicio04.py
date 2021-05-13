nota1 = int(input("ingrese primera nota"))
nota2 = int(input("ingrese segunda nota"))
nota3 = int(input("ingrese tercera nota"))

promedio = round((nota1 + nota2 + nota3) / 3,2)

#round( valor para redondear , cantidad de digito  )

if(promedio >= 6 ):
    print("aprobado")
else:
     print("a diciembre")

print("fin")