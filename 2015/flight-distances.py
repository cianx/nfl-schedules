#!/usr/bin/python
import sys
import requests
import json
import re
import NflData

def getFlightDistance(origin,  dest):
	areokey = "8e9e0117817222135a07143f6f05a5d3";
	url = "https://airport.api.aero/airport/distance/{}/{}".format(origin,  dest);

	payload = { 'user_key': areokey,  "units":"mile" }
	r = requests.get(url,  params = payload)
	print origin,  dest, r.text
	# r.status_code == requests.codes.ok
	# r.raise_for_status()
	p=re.compile('^callback\((.*)\)$')
	return float(json.loads(p.match(r.text).group(1))['distance'].replace(',', ''))

# print getFlightDistance('sea', 'sfo')


stadiums=NflData.Stadiums();
distances=NflData.StadiumDistances();

# add any missing distances. - due to the london issue in the driving matrix. 
for o in stadiums:
	for d in stadiums:
		if not o['Team']==d['Team']:
			if not distances.MakeKey(o['Team'], d['Team']) in distances:
				distances.AddItem({
						'Origin': o['Team'], 
						'Destination': d['Team'], 
					})
				
distances.Write()

#flydistances=NflData.StadiumDistances('2015_NFL_StadiumFly.csv')
#for k in distances:
#	distances[k]["FlightDistance"] = flydistances[k]["FlightDistance"];
#distances.Write()
#exit()
#add the flight distatnces
for k in distances:
	
	e = distances[k]
	print k, e['Origin']
	a1=stadiums[e['Origin']]['AirportCode']
	a2=stadiums[e['Destination']]['AirportCode']
	distances[k]["FlightDistance"] = getFlightDistance(a1,  a2);

distances.Write()

 
exit()




