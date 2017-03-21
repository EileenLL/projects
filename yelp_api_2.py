from json import load
from urllib2 import urlopen
from yelp.config import API_HOST
from yelp.endpoint.business import Business
from yelp.endpoint.search import Search
from yelp.config import SEARCH_PATH
from yelp.obj.search_response import SearchResponse
from yelp.errors import ErrorHandler
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

# read API keys
with open('config_secret.json') as cred:
    creds = load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

location = 'San Francisco'  #raw_input("Please enter your zip code: ")

params = {
    'term': 'dogs allowed',
    'limit': '3'
}

search_response = client.search(location, **params)

class Location(ResponseObject):

    _fields = [
        'postal_code'
    ]

class SearchResponse(ResponseObject):

    _fields = [
        'name'
    ]

SEARCH_PATH = '/v2/search/'

class Search(object):

    def __init__(self, client):
        self.client = client

    def search(self, location, **url_params):

	url_params = {'location':'location'}

	return SearchResponse(self.client._make_request(SEARCH_PATH, url_params))

search_yelp_apiUrl = "https://api.yelp.com/v2/search?term=dogs+allowed&location='location'"

# restaurants_yelp_apiUrl =
print search_yelp_apiUrl

#virtualenv env
#pip install yelp
#python -i yelp_api.py
#search_response.businesses
#dir
#[business.name for business in search_response.businesses]