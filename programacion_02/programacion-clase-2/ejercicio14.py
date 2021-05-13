dia = int(input("ingrese el dia:"))
mes = int(input("intrese el mes:"))

if(dia <=31 or dia >= 1 and mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    print("La fecha es correcta")
elif(dia <=30 or dia >= 1 and mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("la fecha es correcta")
elif(dia <=29 or dia >= 1 and mes == 2):
    print("la fecha es correcta")
else:
    print("la fecha no es correcta")

print("fin")