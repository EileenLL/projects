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

from urllib2 import (
    HTTPError,
    quote,
    urlencode,
)

PI_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
TOKEN_PATH = '/oauth2/token'
GRANT_TYPE = 'client_credentials'

DEFAULT_TERM = 'restaurant'
DEFAULT_LOCATION = 'location'
SEARCH_LIMIT = 3

