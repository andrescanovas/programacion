monto = float(input("ingrese el monto"))
tarjeta = input("ingrese tarjeta")

if(tarjeta == "visa"):
    recargo_visa = 7 * monto / 100
    print("monto totoal", recargo_visa)
elif(tarjeta == "mastercard"):
    recargo_mastercard = 11 * monto / 100
    print("el monto total es:", recargo_mastercard)
else:
    print("monto total", monto)
