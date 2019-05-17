import json
import requests
url1="http://api.openweathermap.org/data/2.5/weather?q="
loc=input("enter the location")
key="&appid=e15ff4bc0377e20b1146518a0471c019"
url=url1+loc+key
response=requests.get(url)
json_data=response.json()
temp=(json_data["main"]["temp"])
print(json_data["weather"][0]["main"]+ " conditions and temp is " ,temp-273 )