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
def print_weather_info(weather_data):
    if weather_data:
        wind_speed = weather_data['wind']['speed']
        temperature = weather_data['main']['temp']
        sun_ray_intensity = weather_data['main']['feels_like'] 
        solar_panel_efficiency = 0.50  
        solar_panel_area = 5000  
        wind_turbine_efficiency = 0.35  
        air_density = 1.225  

        time = 8760 
