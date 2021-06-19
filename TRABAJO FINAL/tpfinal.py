import requests


def get_weather_city(ruta,parametros):
    req = requests.get(url=ruta,params=parametros)
    # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
    if req.status_code == 200:
        dic = req.json()
        return dic
    else:
        print('nope')

opcion=''
while opcion!= 3:
    print('Presione 1 si desea saber los datos actuales')
    print('Presione 2 si desea saber el pronostico')
    print('presione 3 si desea salir')


    opcion = int(input('seleccione su opcion: '))

    if(opcion == 1):
        city = input('ingrese el nombre de la ciudad: ')

        parametros = {}
        parametros['q'] = city
        parametros['units'] = 'metric'
        parametros['lang'] = 'sv, se'
        parametros['appid'] = '1f2000a47cfe64fd14b6f93c69adaf13'

        urlbase = 'https://api.openweathermap.org/data/2.5/weather'


        urlfinal = get_weather_city(urlbase,parametros)

        print(urlfinal['main'])
            # urlfinal['main']

        print()
        print()
        print()

    elif(opcion == 2):

        lat= input("Ingresar la latitud: ")
        lon =  input("Ingresar la longitud: ")
        params  = {}
        params["lat"] = lat
        params["lon"] = lon
        params["units"] = "metric"
        params["appid"] = "1f2000a47cfe64fd14b6f93c69adaf13"

        url_coordenadas = "http://api.openweathermap.org/data/2.5/weather"

        clima = get_weather_city(url_coordenadas,params)

        print('Nombre',clima['name'],clima["main"])
      
        print()
      
    elif(opcion == 3):
        print('EL PROGRAMA A FINALIZADO')

        print()

    else:
        print('Por favor ingrese una opcion valida')