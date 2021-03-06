from pyowm import OWM 

owm = OWM('7c3de8493dbc84d75217e42557436abb')  # You MUST provide a valid API key

place = input("В каком городе/стране?")

mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather 
wind = w.wind()["speed"] 
humidity = w.humidity 
print("В городе " + place + " сейчас " + str(w.temperature('celsius')) + " градусов")
print("Влажность воздуха {}%".format(humidity))
print("Скрость ветра " + wind + " в метрах в секунду")  