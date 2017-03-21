# api_key = iACw3KGROnBuMWPtAUAVHTkil9OB1YfG

from json import load
from urllib2 import urlopen

zipcode = 94606

location_weather_apiUrl = "http://dataservice.accuweather.com/locations/v1/search?apikey=iACw3KGROnBuMWPtAUAVHTkil9OB1YfG&q=94606"

# current_weather_apiUrl = 

response = response.get(location_weather_apiUrl)

json_obj = load(response)

print json_obj



# curl -X GET "http://dataservice.accuweather.com/locations/v1/search?apikey=iACw3KGROnBuMWPtAUAVHTkil9OB1YfG&q=zip%20code"