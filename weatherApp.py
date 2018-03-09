import urllib.request,json

url = "https://api.openweathermap.org/data/2.5/weather?appid=enter api key from owa here=city goes here"

req= urllib.request.Request(url)
print(urllib.request.urlopen(req).read())
