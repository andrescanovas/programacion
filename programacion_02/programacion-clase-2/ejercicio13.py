numero1 = int(input("ingrese el primer numero:"))
numero2 = int(input("ingrese el segundo numero:"))
numero3 = int(input("ingrese el tercer numero:"))

if(numero1 > numero2 and numero1 > numero3):
    print("El numero", numero1 , "es el mayor")
elif(numero2 > numero1 and numero2 > numero3):
        print("El numero", numero2 , "es el mayor")
else:
            print("El numero" , numero3 ,"es el mayor")
print("fin")