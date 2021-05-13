cuenta_del_hotel = int(input("ingrese el la factura del hotel:  "))

ivan = 40 * cuenta_del_hotel / 100
german = 33 * cuenta_del_hotel / 100
esteban = 55 * ivan / 100
hernan = cuenta_del_hotel - german - ivan - esteban

print("el cosuto de ivan es: ", ivan,"el costo de german es: ", german,"el costo de esteban es: ", esteban, "el costo de hernan es: ", hernan)