import json
import requests
url1="https://free.currconv.com/api/v7/convert?q="
str1=input("enter the currency to change")
url2="&compact=ultra&apiKey=848ccb1b6231f6160501"
url=url1+str1+url2
response=requests.get(url)
json_data=response.json()
print("the value  is",json_data[str1])