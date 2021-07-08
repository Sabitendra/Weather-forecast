import pyowm

owm = pyowm.OWM('eaa3ce35e39abba33769a0af0bf54659')
city=input("enter city name : ")
observation = owm.weather_at_place(city)
w = observation.get_weather()
#print(w)

# Weather details
print(w.get_wind())
#print(w.get_humidity())
#print(w.get_temperature('celsius'))
print(w.get_detailed_status())
print(w.get_rain())
print(w.get_weather_icon_name)
print(w.get_pressure())