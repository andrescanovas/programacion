pri_numero = float(input("ingrese el primer numero:"))
seg_numero = float(input("ingrese el segundo numero:"))

if(pri_numero > seg_numero):
    print(pri_numero - seg_numero)
elif(seg_numero > pri_numero):
    print(seg_numero - pri_numero)
else:
    print("los numeros son iguales")

print("fin")