monto = float(input("ingrese el monto:"))
tarjeta = input("ingrese tarjeta:")
cuotas = int(input("ingrese cantidad de cuotas:"))


if(couotas == 3):
    monto = 3 * cuotas/ 100
elif(cuotas == 8):
    monto = 17 * monto / 100
elif(cuotas == 12 ):
    monto = 32 * monto / 100

if(tarjeta == "visa"):
    recargo_visa = 7 * monto / 100
    print("monto totoal", recargo_visa)
elif(tarjeta == "mastercard"):
    recargo_mastercard = 11 * monto / 100
    print("el monto total es:", recargo_mastercard)
else:
    print("monto total", monto)
