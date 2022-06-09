# Write a Django Function to Connect With Weather API & Fetch The Latest Weather Information & Display That.

import requests,json

# MY API KEY
apiKey = "6e38def826455fa934b9eebc54690ec8"

# URL
url = "https://api.openweathermap.org/data/2.5/weather?q="

# CITY (Fetch The Latest Weather Information)
city = input("Enter your city :")

# MAIN URL
commonUrl = url + city + "&appid=" + apiKey

# Connection With Weather API
responce = requests.get(commonUrl)
data = responce.json()

print("current Temprature of :",data["main"]["temp"])
print("current Temprature Feels like :",data["main"]["feels_like"])
print("Maximum Temprature :",data["main"]["temp_max"])
print("minimum Temprature : ",data["main"]["temp_min"])
