# !/usr/bin/env python
import requests
import json
import os

from time import sleep
from pprint import pprint

API_KEY = os.environ['API_KEY_GOOGLE_PLACES']
LAT = 25.7742658 #Miami
LONG = -80.1936589 #Miami
LOCATION = "{},{}".format(LAT, LONG)
RADIUS = 15000 #1.5 km
TYPE = "doctor"

loop_true = True
while loop_true:

    r = requests.get("""https://maps.googleapis.com/maps/api/place/textsearch/json?location={}&radius={}&type={}&key={}""".format(LOCATION, RADIUS, TYPE, API_KEY))
    data = r.content.decode("utf-8")
    data = json.loads(data)

    if len(data['results']) > 0: #If the API returned at least a result
        for index in range(len(data["results"])):
            try:
                place_id = data['results'][index]['place_id'] #get the place_id for the current index of result
                types = data['results'][index]['types'] #get the type(s) for the current index of result
            except Exception as e:
                print(e)
                print("problem setting place_id, types")
            sleep(45)

            r = requests.get("""https://maps.googleapis.com/maps/api/place/details/json?place_id={}&key={}""".format(place_id, API_KEY)) #get place details for the current index of result
            data = r.content.decode("utf-8")
            data = json.loads(data)

            try:
                name = data['result']['name'] #get the name from place details
                address = data['result']['formatted_address'] #get the formatted address from place details
                phone_number = data['result']['international_phone_number'] #get the international phone number from place details
                website = data['result']['website'] #get the website from place details
                print(name, address, phone_number, website)
            except Exception as e:
                print(e)
                print("problem setting name, address, phone_number, website")
    else:
        sleep(5) # If the first call did not return any result, probably due to API rate limit.
        