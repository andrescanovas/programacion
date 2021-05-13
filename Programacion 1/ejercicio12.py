kilowatt = int(input("ingresar cantidad de kilowatt"))
segundos = int(input("ingresar cantidad de segundos"))

kilowatt_por_seg = kilowatt * segundos

impuesto21 = 0.21 * kilowatt_por_seg / 100

promocion = 3.7 * kilowatt_por_seg / 100

total = float(kilowatt_por_seg + impuesto21) - promocion

print("el total es :", total)

