from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=3842242fbbed128879e5973bbc483a75'
    city='hyderabad'
    r= requests.get(url.format(city)).json()
   
    
    
    
    weather = {
        'city': city.lower(),
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
        'wind': r['wind']['speed'],
        'country':r['sys']['country']
    }
    print(weather)
    context = {'weather':weather}
    return render(request, 'weather.html',context)
    