nombreyapellido_persona1 = input("ingrese nombre de la primera persona")
edad_persona1 = int(input("ingrese edad de la primera persona"))

nombreyapellido_persona2 = input("ingrese nombre de la segunda persona")
edad_persona2 = int(input("ingrese edad de la segunda persona"))

nombreyapellido_persona3 = input("ingrese nombre de la tercera persona")
edad_persona3 = int(input("ingrese edad de la tercera persona"))



if(edad_persona1 >= 20):
    print(nombreyapellido_persona1, "es apto")
else:
    print(nombreyapellido_persona1, "no es apto")
if(edad_persona2 >= 20):
    print(nombreyapellido_persona2, "es apto")
else:
    print(nombreyapellido_persona2, "no es apto")
if(edad_persona3 >= 20):
    print(nombreyapellido_persona3, "es apto")
else:
    print(nombreyapellido_persona3, "no es apto")

if(edad_persona1 and edad_persona2 and edad_persona3 < 20):
    print("nadie es apto")


print("fin")
