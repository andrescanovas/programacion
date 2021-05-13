minutos = int(input("ingrese duracion de llamada:"))
costo_minuto = int(input("ingrese costo por minuto:"))

total_de_la_llamada = minutos * costo_minuto

adicional = 5 * total_de_la_llamada / 100

total = total_de_la_llamada + adicional

print("EL TOTAL A PAGAR ES:" , total)
