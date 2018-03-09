import urllib.request,json

url = "https://api.openweathermap.org/data/2.5/weather?appid=2cfcab02ad439f3aa0dcfc20fd116ce7&q=Baton Rouge"

req= urllib.request.Request(url)
print(urllib.request.urlopen(req).read())
