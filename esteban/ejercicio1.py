personaje1 = input('ingrese el nombre del primer pesonaje: ')
altura1 = int(input('ingrese la altura del primer personaje: '))
peso1= int(input('ingrese el peso del primer personaje: '))
planetanatal1 = input('ingrese el planeta natal de primer personaje: ')
peliculas1 = int(input('ingrese la cantidad de peliculas del primer personaje: '))

personaje2 = input('ingrese el nombre del segundo pesonaje: ')
altura2 = int(input('ingrese la altura del segundo personaje: '))
peso2= int(input('ingrese el peso del segundo personaje: '))
planetanatal2 = input('ingrese el planeta natal de segundo personaje: ')
peliculas2 = int(input('ingrese la cantidad de peliculas del segundo personaje: '))


if(altura1 > altura2 ):
    print('El personaje',personaje1,'es mas alto, con una altura de',altura1,'que el',personaje2,'con una altua de ', altura2)
elif(altura2 > altura1 ):
    print('El personaje',personaje2,'es mas alto, con una altura de',altura2,'que el',personaje1,'con una altua de ', altura1)
else:
    ('Ambos personajes tienen la misma altura')


if(peso1 > peso2 ):
    print('El personaje',personaje1,'es mas pesado, con un peso de',peso1,'que el',personaje2,'con un peso de ', peso2)
elif(peso2 > peso1 ):
    print('El personaje',personaje2,'es mas pesado, con un peso de',peso2,'que el',personaje1,'con un peso de ', peso2)
else:
    ('Ambos personajes tienen el mismo peso')


if(peliculas1 > peliculas2 ):
    print('El personaje',personaje1,'participo en mas peliculas con un total de',peliculas1,'que el',personaje2,'que tiene ', peliculas2)
elif(peliculas2>peliculas1):
    print('El personaje',personaje2,'participo en mas peliculas con un total de',peliculas2,'que el',personaje1,'que tiene ', peliculas1)

else:
    ('Ambos personajes tienen la misma cantidad de peliculas')

print('El personaje ',personaje1, ' es originario de ',planetanatal1)

print('El personaje ',personaje2, ' es originario de ',planetanatal2)


if(personaje1 == 'yoda' or personaje1 == 'chuwaka'):
    print(personaje1)
elif(personaje2 == 'yoda' or personaje2 == 'chuwaka'):
    print(personaje2)