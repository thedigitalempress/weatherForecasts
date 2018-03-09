import urllib.request,json
 
city = input("Enter City: ")
 
def getForecast(city):
    url = "https://api.openweathermap.org/data/2.5/weather?appid=enter api key from owa here="
    url = url + city
    req = urllib.request.Request(url)
    response=urllib.request.urlopen(req)
    data = response.read()
    return json.loads(data.decode("UTF-8"))
 
forecast = getForecast(city)
 
print("Forecast for", city, forecast['sys']['country'])
 
print("Description:", forecast['weather'][0]['description'])
print("Temp:", forecast['main']['temp'])
print("Pressure:", forecast['main']['pressure'])
print("Humidity:", forecast['main']['humidity'])
print("Wind Speed:", forecast['wind']['speed'])
