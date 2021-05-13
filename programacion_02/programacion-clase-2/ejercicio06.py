primernumero = int(input("ingrese el primer numero"))
segundonumero = int(input("ingrese el segundo numero"))



if(primernumero > segundonumero):

    print("es primer mayor que", segundonumero)
else:
    if(primernumero < segundonumero):
        print("es primero menor que", segundonumero)
    else:
        print("los numero son iguales")

    print("fin")