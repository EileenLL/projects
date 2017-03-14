#yelp

# API v2.0
# Consumer Key	ouxv9UaUrjZjukvuWLGo3A
# Consumer Secret	j8_ZSLjsiIZGuzal5J-EGaCD-kY
# Token	pl9cB_9Rda1yV5FF1GNYXWVOLXVgjWh8
# Token Secret	6Pwsh_ZjqrEO3X79VS1idnu3gfE

# Fusion
# App ID
# 62Uz70gNEVYGxGx9v3FdxQ
# App Secret
# vnXfbMdjffORLSRnEkRVeBeTAK6JfClUut7UCmJtmlrkVVudv9aGQuudd93quvnq

# GET https://api.yelp.com/v3/businesses/search


#AccuWeather

#CodingTime1!

# API Key	iACw3KGROnBuMWPtAUAVHTkil9OB1YfG
# Key Issued	Tue, 03/07/2017 - 15:10

# read API keys



GET https://api.yelp.com/v3/businesses/search

yelp_api = vnXfbMdjffORLSRnEkRVeBeTAK6JfClUut7UCmJtmlrkVVudv9aGQuudd93quvnq

weather_api = iACw3KGROnBuMWPtAUAVHTkil9OB1YfG




#user inputs location zip code
#weather function looks at weather api for inputed location
#if the temp is below 65 degrees print "It's a little cold, lets order in."
#if the temp is above 90 degrees print "It's too hot, your pup should stay home."
#if it is clear or overcast skys and within 65 - 90 degrees run restaurant function
#else print "Uh oh! This weather looks bad, let's go out another day"
#restaurant function checks local restaurants list, sorted by best match for "Dogs Allowed" feature
#creates a new list of top five restaurants 
#print "The weather is perfect! We could go to: " dog_restaurant_list

from urllib2 import HTTPError
from urllib import quote
from urllib import urlencode

PI_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
TOKEN_PATH = '/oauth2/token'
GRANT_TYPE = 'client_credentials'

DEFAULT_TERM = 'restaurant'
DEFAULT_LOCATION = 'location'
SEARCH_LIMIT = 3

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

