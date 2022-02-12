import requests
import json


def data(city):

    #OpenweathermapAPI  
    api_key = "159ca327a8c228c01eadfa4d194b50c2"

    #Sample API Call
    weather_data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}').json()

    ##uncomment the code below to print a nicely formatted dictionary of the API 
    #nice_format = json.dumps(weather_data, indent=4)

    data_dict = {
        "name": str(weather_data['name']),
        "temp": str(weather_data['main']['temp']),
        "country": str(weather_data['sys']['country']),
        "feels_like": str(weather_data['main']['feels_like']),
        "max_temp": str(weather_data['main']['temp_max']),
        "min_temp": str(weather_data['main']['temp_min']),
        "weather_char": str(weather_data['weather'][0]['description']),
        "icon": str(weather_data['weather'][0]['icon'])
    }

    return data_dict
       
