#!/usr/bin/python
import sys
import datetime
import NflData



stadiums = NflData.Stadiums()
distances = NflData.StadiumDistances()
schedule = NflData.Schedule()

for i in range(1, 18):
	print "Week", i
	games = schedule.GetWeekGames(i)
	tg=[]
	ug=[]
	sg=[]
	mg=[]
		
	for g in games:
		if g['Date'].weekday() == 3:
			tg.append(g)
		if g['Date'].weekday() == 5:
			ug.append(g)
		if g['Date'].weekday() == 6:
			sg.append(g)
		if g['Date'].weekday() == 0:
			mg.append(g)
	if len(sg) == 0:
		print "Error no sunday games."

	for tng in tg:
		for sdg in sg:
			for mng in mg:
				tsd = int(distances.DriveDistance(tng['Home'], sdg['Home']))
				smd = int(distances.DriveDistance(mng['Home'], sdg['Home']))
				mtd = int(distances.DriveDistance(tng['Home'], mng['Home']))
				if(tsd <= 750 and smd  <= 750):
					print tng['Tag'], tsd, \
						sdg['Tag'], smd, \
						mng['Tag'], mtd 

exit()




