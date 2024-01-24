import requests
from geopy.geocoders import Nominatim
# API key you obtained from OpenWeatherMap
API_KEY = 'b6055519348badd5c7c69b3b7f191c94'


def get_weather_data(area):
    geolocator = Nominatim(user_agent="MyApp")

    location = geolocator.geocode(area)

    #print("The latitude of the location is: ", location.latitude)
    #print("The longitude of the location is: ", location.longitude)
    lat = location.latitude
    lon = location.longitude
    base_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
  
    response = requests.get(base_url)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None
