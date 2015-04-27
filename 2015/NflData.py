import csv
import os


class Stadiums:
	def __init__(self, name='2015_NFL_Stadiums.csv'):
		stadiums = []
		stadiumMap = {}
		self.name = name;
		if(os.path.exists(name)):
			idx = 0
			with open(name, 'rU') as csvfile:
				creader = csv.DictReader(csvfile,  delimiter=',',  quotechar='"');
				for row in creader:
					row['Address'] = ",".join([row['StreetAddress'], row['City'], row['State'], row['ZIP']])
					stadiums.append(row)
					stadiumMap[row['Team']] = idx
					idx=idx+1
			self.stadiums = stadiums
			self.stadiumMap = stadiumMap
			
	def __len__(self):
		return len(self.stadiums)
	
	def __getitem__(self, idx):
		if isinstance(idx, int):
			return self.stadiums[idx]
		else:
			return self.stadiums[self.stadiumMap[idx]]
		
	def __iter__(self):
		return self.stadiums.__iter__();

def num(x):
	try:
		if x=="":
			return 0;
		return float(x)
	except:
		return 0


class StadiumDistances:
	def __init__(self, name='2015_NFL_StadiumDistances.csv'):
		distances = {}
		self.name = name;
		if(os.path.exists(name)):
			with open(name, 'rU') as csvfile:
				creader = csv.DictReader(csvfile,  delimiter=',',  quotechar='"');
				for row in creader:
					key = "{}-{}".format(row['Origin'],row['Destination'])
					if 'DriveTime' in row:
						row['DriveTime'] = num(row['DriveTime'])
					if 'DriveDistance' in row:
						row['DriveDistance'] = num(row['DriveDistance'])
					if 'FlightDistance' in row:
						row['FlightDistance'] = num(row['FlightDistance'])
					else:
						row['FlightDistance'] = 0
					distances[key] = row
		self.distances = distances
			
	def __getitem__(self, idx):
		return self.distances[idx]
	
	def __contains__(self, idx):
		return self.distances.has_key(idx)
	
	def __iter__(self):
		return self.distances.__iter__();

	def MakeKey(self, o, d):
		if(o<d): 
			key="{}-{}".format(o,d)
		else:
			key="{}-{}".format(d,  o)
		return key;
	
	def GenKey(self, dist):
		o = dist['Origin']
		d = dist['Destination']
		if(o<d): 
			key="{}-{}".format(o,d)
		else:
			key="{}-{}".format(d,  o)
			dist['Origin']=d
			dist['Destination']=o
		return key;

	def AddItem(self, d):
		self.distances[self.GenKey(d)] = d\

	def Write(self):
		with open(self.name,  'w') as csvfile:
			cwriter = csv.DictWriter(csvfile,  delimiter=',',  quotechar='"',  extrasaction='ignore', quoting=csv.QUOTE_NONNUMERIC, fieldnames= ['Origin',  'Destination',  'DriveTime',  'DriveDistance',  "FlightDistance"])
			cwriter.writeheader()
			for k in self.distances:
				cwriter.writerow(self.distances[k])
		pass;
	


class Schedule:
	def __init__(self, name='2015_NFL_Schedule.csv'):
		schedule = []
		self.name = name;
		if(os.path.exists(name)):
			with open(name, 'rU') as csvfile:
				creader = csv.DictReader(csvfile,  delimiter=',',  quotechar='"');
				for row in creader:
					schedule.append(row)
			self.schedule = schedule;

