from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

# Create your views here.
def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'New York'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3cf482fe50e82bd2b670a3bb2992bb68'
    PARAMS = {'units':'metric'}

    API_KEY = 'AIzaSyCrYhgWSfr41UtEwE-fI7fW4BMC7-3FOr8'

    SEARCH_ENGINE_ID = '7462ef0788eb245cd'
     
    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']
    
    try:
        data = requests.get(url,PARAMS).json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        day =datetime.date.today()

        return render(request,'weather_app/index.html',{'description':description, 'icon':icon, 'temp':temp, 'day':day, 'city':city,'exception_occurred':False ,'image_url':image_url,'app_name': '🌤️ My Custom Weather App 🌦️'})
    
    except:
        exception_occurred=True
        messages.error(request,'Entered data is not available to API')
        day=datetime.date.today()

        return render(request,'weather_app/index.html',{'description':'clear sky', 'icon':'01d', 'temp': 25, 'day':day, 'city':'New York','exception_occurred':exception_occurred,'app_name': '🌤️ My Custom Weather App 🌦️'})
    

   

