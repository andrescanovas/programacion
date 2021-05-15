from random import randint

numero = []

for i in range (0,78):
    num = randint(1,78)
    numero.append(num)

numero.sort()

print ("El menor es ",numero[0])
print ("El mayor es ",numero[77])

print(numero)
for numero in range (0,78):
    if (numero % 2==0):
        print(numero)



