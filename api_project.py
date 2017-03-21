

yelp_api = vnXfbMdjffORLSRnEkRVeBeTAK6JfClUut7UCmJtmlrkVVudv9aGQuudd93quvnq

weather_api = iACw3KGROnBuMWPtAUAVHTkil9OB1YfG

from flask import Flask
from json import load
from urllib2 import urlopen
from yelp_api import search_yelp_apiUrl

curl -X GET "http://dataservice.accuweather.com/locations/v1/search?apikey=iACw3KGROnBuMWPtAUAVHTkil9OB1YfG&q=zip%20code"

location_key = http://api.accuweather.com/locations/v1/335315.json?apikey={weather_api}

location = raw_input("What is your current zip code? ")
#weather_api location key

def whats_the_temp():
  temp = #inport temp from weather_api
  if temp < 65:
    print "It's a little cold, lets order in."
  elif temp > 90:
    print "It's too hot, your pup should stay home with lots of water."
  else:
    whats_the_precip()

def whats_the_precip():
	precip = #inport precip from weather_api
	if precip == clear or overcast:
		local_dog_restaurants()
	else:
		print "My knee says a storm is coming, let's leave the pup where it's dry."


def local_dog_restaurants():
	#restaurant function checks local restaurants list, sorted by best match for "Dogs Allowed" feature
#creates a new list of top five restaurants 
#print "The weather is perfect! We could go to: " dog_restaurant_list

https://api.yelp.com/v2/search?term=food&location=San+Francisco
location=location
