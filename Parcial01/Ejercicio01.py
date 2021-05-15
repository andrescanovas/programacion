from consumo_api import get_charter_by_id

from random import randint

num1 = randint(1,83)
num2 = randint(1,83)
p1 = get_charter_by_id(num1)
p2 = get_charter_by_id(num2)


def altura(item):
    if(item['height'].isdecimal()):
        return int(item['height'])
    else:
        return -1
def peso(item):
    if(item['mass'].isdecimal()):
        return float(item['mass'])
    else:
        return -1


print('Entre los personajes',p1['name'],'y',p2['name'])
if (altura(p1) > altura(p2)) :
   print ("El  alto es",p1["name"],"la altura del personaje es ", altura(p1))
else:
    print ("El alto es",p2["name"],"la altura del personaje es ", altura(p2))
if (peso(p1)) > (peso(p2)):
   print ("El que es mas pesado es",p1["name"],"el peso del personaje es ", altura(p1))
else:
    print ("El que es mas pesado es",p2["name"],"el peso del personaje es ", altura(p2))
print(p1['name'],'tiene',len(p1['films']),'peliculas','y',p1['name'],'tiene',len(p2['films']),'peliculas')
    

    

