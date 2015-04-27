#!/usr/bin/python
import sys
import googlemaps
import requests
import json
import re
import NflData

gmaps = googlemaps.Client(key="AIzaSyDDyj1jsV9ZePA7Pv8Ku3ZlhGw4qs_UE-Y")

# addrs is expected to be a map of key, address pairs 
# return will be  map key: { key: { duration: hours, distance: miles}, ... }
def getDrivingDistance(stadiums):
	keys= []
	addrs= []
	for t in stadiums:
		keys.append(t['Team'])
		addrs.append(t['Address'])
		
	out = NflData.StadiumDistances()
	for i in range(len(keys)):
		o = keys[i]
		try:
			result = gmaps.distance_matrix(addrs[i:i+1],  addrs)
		except:
			print "gmaps distance matrix error: " , sys.exc_info()[0]
			raise

		r = result['rows'][0]['elements']
		for j in range(len(keys)):
			e = r[j]
			d = keys[j]
			if e['status'] == 'OK' and o != d:
				out.AddItem({
						'Origin': o, 
						'Destination': d, 
						'DriveTime': int(e['duration']['value'])/(60.*60.), 
						'DriveDistance': int(e['distance']['value'])*0.000621371,
					})
			else:
				if o != d:
					print "Error on {} {}".format(o, d), e
	return out
	
stadiums=NflData.Stadiums();

dist = getDrivingDistance(stadiums)
dist.Write()
exit()
