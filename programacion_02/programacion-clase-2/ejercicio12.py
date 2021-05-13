numero_del_mes = int(input("ingrese el numero del mes:"))

if(numero_del_mes == 1 or numero_del_mes == 3 or numero_del_mes == 5 or numero_del_mes == 7 or numero_del_mes == 8 or numero_del_mes == 10 or numero_del_mes == 12):
    print("El mes tiene 31 dias")
elif(numero_del_mes == 4 or numero_del_mes == 6 or numero_del_mes == 9 or numero_del_mes == 11):
    print("El mes tiene 30 dias")
elif(numero_del_mes == 2):
    print("El mes tiene 28 dias")
else:
    print("Ese mes no existe")

print("fin")