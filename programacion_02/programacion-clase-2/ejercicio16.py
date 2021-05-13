dia = int(input("ingrese dia dd:"))
mes = int(input("ingrese mes mm"))
anio = int(input("ingrese año aa"))


if(dia < 31 and dia >= 1 and  mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10):
    print(dia + 1, mes, anio)
elif(dia == 31 and  mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10):
    print( "1", mes + 1, anio)
elif(dia == 31 and mes == 12):  
    print("1","1",anio +1)
elif(dia == 30 and mes == 12):
    print("31", mes ,anio)
elif(dia < 30 and dia >= 1 and  mes == 1 or mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print(dia + 1, mes, anio)
elif(dia == 30 and  mes == 1 or mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print( "1", mes + 1, anio)
elif(dia < 28  and dia >= 1 and mes == 2):
    print(dia + 1, mes, anio)
elif(dia == 28 and  mes == 2):
    print( "1", mes + 1, anio)
else:
    print("ingrese una fecha o valide el formato ingresado")
print("fin")
