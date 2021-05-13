cartanumero1 = int(input("ingrese el valor de la PRIMERA carta:"))
cartapalo1 = input("ingrese el palo de la PRIMERA carta:")
cartanumero2 = int(input("ingrese el valor de la SEGUNDA carta:"))
cartapalo2 = input("ingrese el palo de la SEGUNDA carta:")
cartanumero3 = int(input("ingrese el valor de la TERCERA carta:"))
cartapalo3 = input("ingrese el palo de la TERCERA carta:")


if(cartapalo1 == cartapalo2 and cartapalo1 == cartapalo3):
    print("FLOR")
elif(cartapalo1 == cartapalo2):
    print("ENVIDO", cartanumero1 + cartanumero2)
elif(cartapalo1 == cartanumero3):
    print("envido", cartanumero1 + cartanumero3)
elif(cartapalo2 == cartapalo3):
    print("Envido", cartanumero2 + cartanumero3)

else:
    print("no tenes nada")

print("fin")