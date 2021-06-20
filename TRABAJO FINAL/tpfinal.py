import requests


def get_weather_city(ruta,parametros):
    req = requests.get(url=ruta,params=parametros)
    # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
    if req.status_code == 200:
        dic = req.json()
        return dic
    else:
        print('nope')

import requests

def get_weather_city(ruta,parametros):
    req = requests.get(url=ruta,params=parametros)
    # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
    if req.status_code == 200:
        dic = req.json()
        return dic
    else:
        print('nope')



# -----------------------------------------------------------------------------------------------------------------------





opcion=''
while opcion!= '0':
    print('Presione 1 si desea saber los datos actuales con nombre de la ciudad/pais')
    print('Presione 2 si desea saber los datos actuales con coordenadas')
    print('Presione 3 si desea saber los datos en 4 dias')
    print('Presione 4 si desea saber los datos en 4 dias "Solo con coordenadas"')
    print('presione 0 si desea salir')


    opcion = input('seleccione su opcion: ')
    
    if(opcion == '1'):
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

    elif(opcion == '2'):

        lat= input("Ingresar la latitud: ")
        lon =  input("Ingresar la longitud: ")
        params  = {}
        params["lat"] = lat
        params["lon"] = lon
        params["units"] = "metric"
        params["appid"] = "1f2000a47cfe64fd14b6f93c69adaf13"

        url_base= "http://api.openweathermap.org/data/2.5/weather"

        clima = get_weather_city(url_base,params)

        print('Nombre',clima['name'],clima["main"])
      
        print()


 # ver pronostico 4 dias ciudad
    elif (opcion == '3' ):
        ciudad = input("Ingresar una ciudad para pronostico de 4 dias: ")
        params  = {}
        params["q"] = ciudad
        params["appid"] = "1f2000a47cfe64fd14b6f93c69adaf13"
        params["units"] = "metric"
        

        url = "https://api.openweathermap.org/data/2.5/forecast"

        clima = get_weather_city(url,params)

        print()
       
        fecha = clima["list"][1]["dt_txt"]
        datos = clima["list"][1]

        print("El tiempo para el dia",fecha,'en',ciudad, "es de: ")
        print (datos)


        fecha = clima["list"][13]["dt_txt"]
        datos = clima["list"][13]
        print()
        print("El tiempo para el dia",fecha,'en',ciudad, "es de: ")
        print (datos)

        fecha = clima["list"][20]["dt_txt"]
        datos = clima["list"][20]
        print()
        print("El tiempo para el dia",fecha,'en',ciudad, "es de: ")
        print (datos)

        fecha = clima["list"][27]["dt_txt"]
        datos = clima["list"][27]
        print()
        print("El tiempo para el dia",fecha,'en',ciudad, "es de: ")
        print (datos)

        fecha = clima["list"][35]["dt_txt"]
        datos = clima["list"][35]
        print()
        print("El tiempo para el dia",fecha,'en',ciudad, "es de: ")
        print (datos)

    elif(opcion == '4'):
        lat= input("Ingresar la latitud: ")
        lon=  input("Ingresar la longitud: ")
        params  = {}
        params["lat"] = lat
        params["lon"] = lon
        params["units"] = "metric"
        params["appid"] = "1f2000a47cfe64fd14b6f93c69adaf13"

        url_base = "https://api.openweathermap.org/data/2.5/forecast"

        clima = get_weather_city(url_base,params)
        
        fecha = clima["list"][1]["dt_txt"]
        datos = clima["list"][1]
        
        print()


        print("El tiempo para el dia",fecha,' en la latitud',lat,' y en la lon',lon," es de: ")
        print (datos)

        fecha = clima["list"][13]["dt_txt"]
        datos = clima["list"][13]
        print()

        print("El tiempo para el dia",fecha,' en la latitud',lat,' y en la lon',lon, "es de: ")
        print (datos)
        fecha = clima["list"][20]["dt_txt"]
        datos = clima["list"][20]
        
        print()
        
        print("El tiempo para el dia",fecha,' en la latitud',lat,' y en la lon',lon, "es de: ")
        print (datos)
        fecha = clima["list"][27]["dt_txt"]
        datos = clima["list"][27]

        print()    

        print("El tiempo para el dia",fecha,' en la latitud',lat,' y en la lon',lon, "es de: ")
        print (datos)
        fecha = clima["list"][38]["dt_txt"]
        datos = clima["list"][38]
        print()

    elif(opcion == '0'):
        print('EL PROGRAMA A FINALIZADO')

        print()

    else:
        print()
        print('Por favor ingrese una opcion valida')
        print()