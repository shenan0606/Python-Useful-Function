'''
Get distance Example: Need Geopy library and GoogleV3 API Key.
GoogleV3 API Key is not free, but Google provides $300 free credits at the regristration.
# The distance given here is the STRAIGHT-LINE Distance, NOT the driving distance !!!
'''

from geopy.geocoders import GoogleV3
import json
geolocator = GoogleV3(api_key='')
location1 = geolocator.geocode("Address1, City, State", language='en')
location2 = geolocator.geocode("Address2, City, State", language='en')
print((location1.latitude, location1.longitude))

from geopy.distance import geodesic
lat_long1 = (location1.latitude, location1.longitude)
lat_long2 = (location2.latitude, location2.longitude)
print(geodesic(lat_long1, lat_long2).miles)

''' The distance is not absolutly accurate '''
geolocator.geocode('764 Lickskillet Rd, Warrenton, NC 27589, USA', language='en') 
geolocator.geocode('2 Old 75 Hwy, Butner, NC 27509, USA', language='en')
lat_long1 = (location1.latitude, location1.longitude)
lat_long2 = (location2.latitude, location2.longitude)
print(geodesic(lat_long1, lat_long2).miles)
