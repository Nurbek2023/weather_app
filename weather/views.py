import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import City
from .forms import CityForm

def remove_city(request, id):
    item_to_remove = get_object_or_404(City, id=id)

    item_to_remove.delete()

    return redirect('/index')

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=78698daab7ebf11561e2f466be526b35'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        if r.get('main'):
            

            city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            'error': 'False',
            'id': city.id,
        }
        else:
            city_weather = {
                'id': city.id,
                'city': city.name,
                'error': True,
            }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/weather.html', context)