import requests
import os

API_KEY = os.environ['API_KEY_GOOGLE_PLACES']
LAT = 25.7742658
LONG = -80.1936589 
LOCATION = "{},{}".format(LAT, LONG)
RADIUS = 1500
TYPE = "doctor"

r = requests.get("""https://maps.googleapis.com/maps/api/place/textsearch/json?location={}&radius={}&type={}&key={}""".format(LOCATION, RADIUS, TYPE, API_KEY))
data = r.content.decode("utf-8")
