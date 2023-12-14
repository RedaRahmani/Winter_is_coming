# views.py
from django.shortcuts import render
import requests
import datetime

def forecast(request):
    forecast_url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&&units=metric&appid=b8b222d059c95d19b5163e6ef1749a0f'

    current_weather_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=b8b222d059c95d19b5163e6ef1749a0f'
    api_key = 'b8b222d059c95d19b5163e6ef1749a0f'
    
    if request.method == 'POST':
        city = request.POST['city']
        weather_data = get_weather_data(city, api_key, current_weather_url, forecast_url)
        
        if 'city_not_found' in weather_data:
            # Render the same page with an error message
            return render(request, 'weather_app/index.html', {'error_message': 'City not found!'})

        context = {
            'weather_data': weather_data['weather_data'],  # Get weather_data from the returned dictionary
            'forecast_data': weather_data['forecast_data'],  # Get forecast_data from the returned dictionary
        }

        return render(request, 'weather_app/index.html', context)
    else:
        return render(request, 'weather_app/index.html')


def get_weather_data(city, api_key, current_weather_url, forecast_url):
    # daily data through API
    response = requests.get(current_weather_url.format(city, api_key)).json()

    if response['cod'] == '404':
        # City not found
        return {'city_not_found': True}

    lat, lon = response['coord']['lat'], response['coord']['lon']
    # daily weather data
    weather_data = {
        'city': city,
        'temperature': response['main']['temp'],
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        'temperature_max': response['main']['temp_max'],
        'temperature_min': response['main']['temp_min'],
        'feelslike_weather': response['main']['feels_like']
    }

    full_forecast = requests.get(forecast_url.format(city)).json()
    forecast_data = {}
    # today = datetime.datetime.now()
    today_date = datetime.datetime.today().strftime('%d')

    for c in range(0, full_forecast['cnt']):
        date_var1 = full_forecast['list'][c]['dt_txt']
        date_time_obj1 = datetime.datetime.strptime(date_var1, '%Y-%m-%d %H:%M:%S')

        if int(date_time_obj1.strftime('%d')) == int(today_date) or int(date_time_obj1.strftime('%d')) == int(
                today_date) + 1:
            if int(date_time_obj1.strftime('%d')) == int(today_date) + 1:
                today_date = str(int(today_date) + 1)
            forecast_data[today_date] = {
                'day': date_time_obj1.strftime('%A'),
                'date': date_time_obj1.strftime('%d %b, %Y'),
                'time': date_time_obj1.strftime('%I:%M %p'),
                'FeelsLike': full_forecast['list'][c]['main']['feels_like'],
                'temperature': full_forecast['list'][c]['main']['temp'],
                'temperature_max': full_forecast['list'][c]['main']['temp_max'],
                'temperature_min': full_forecast['list'][c]['main']['temp_min'],
                'description': full_forecast['list'][c]['weather'][0]['description'],
                'icon': full_forecast['list'][c]['weather'][0]['icon']
            }
            today_date = str(int(today_date) + 1)

    return {'weather_data': weather_data, 'forecast_data': forecast_data}

def about(request):
    return render(request, 'weather_app/about.html')  # Render the about.html template

# weather_app/views.py
def login(request):
    return render(request, 'weather_app/login.html')

