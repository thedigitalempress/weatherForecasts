import urllib.request,json

city = input("Enter City: ")

def getForecast(city) :
    url = "https://api.openweathermap.org/data/2.5/weather?appid=2cfcab02ad439f3aa0dcfc20fd116ce7&q="
    url = url + city
    req = urllib.request.Request(url)
    response=urllib.request.urlopen(req)
    return json.loads(response.read().decode("UTF-8"))

forecast = getForecast(city)

print("Forecast for ", city, forecast['city']['country'])

day_num=1
for day in forecast['list']:
    print("Day : ", day_num)
    print(day['weather'][0]['description'])
    print("Cloud Cover : ", day['clouds'])
    print("Temp Min : ", round(day['temp']['min']-273.15, 1), "degrees C")
    print("Temp Max : ", round(day['temp']['max']-273.15, 1), "degrees C")
    print("Humidity : ", day['humidity'], "%")
    print("Wind Speed : ", day['speed'], "m/s")
    print()
    day_num = day_num+1
