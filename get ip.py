#!/usr/bin/env python
import sys
import urllib.request
import json
from io import StringIO
import pandas as pd


def get_info(address):  
    api = "http://api.ipstack.com/" + address + "?access_key=00ae38b023482ed978fc7e354465615f"
    try:        
        result = urllib.request.urlopen(api).read()
        result = str(result)
        result = result[2:len(result)-1] 
        result = json.loads(result)
    except:
        print("Could not find: ", address)
        return None 

    return(result)
          

address = "172.118.208.216"
address_info = get_info(address)
print(address)
print("IP: ", address_info["ip"])
print("Country Name: ", address_info["country_name"])
print("Country Code: ", address_info["country_code"])
print("Region Name: ", address_info["region_name"])
print("Region Code: ", address_info["region_code"])
print("City: ", address_info["city"])
print("Zip Code: ", address_info["zip"])
print("Latitude: ", address_info["latitude"])
print("Longitude: ", address_info["longitude"])
print("Location link: " + "http://www.openstreetmap.org/#map=11/" + str(address_info["latitude"]) +"/" + str(address_info["longitude"]))
type(address_info)


