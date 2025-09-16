from django.shortcuts import render
import json 
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=1e1a05cf62bc3a10a12e767d933c4758').read()
        json_data = json.loads(res)
        data = {
            'country_code': str(json_data['sys']['country']),
            'coordinate': f"{json_data['coord']['lon']} {json_data['coord']['lat']}",
            'temp': str(json_data['main']['temp']) + ' K',
            'pressure': str(json_data['main']['pressure']) + ' hPa',
            'humidity': str(json_data['main']['humidity']) + '%',

            }
    else:
        city = ' '
        data = {}
    return render(request, 'index.html',{'city':city,'data':data})