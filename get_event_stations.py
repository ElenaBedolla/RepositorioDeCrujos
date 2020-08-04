from obspy.clients.fdsn import Client
from obspy import UTCDateTime, read
import os
import datetime
import copy
import obspy
import shutil
from pathlib import Path
import re, os, shutil, glob, random
from events import parse_event

end_time = datetime.datetime.now() 
start_time = end_time-datetime.timedelta(hours=24) # Intervalo de busqueda desde 12 horas anteriores a la actual
starttime = UTCDateTime(start_time.isoformat())
print(start_time.isoformat())
endtime = UTCDateTime(end_time.isoformat())

#latitude=15
#longitude=-90
minradius=0
maxradius=10
mindepth = 0
maxdepth = 100
minmagnitude=5
maxmagnitude=10
max_sta = 5
tmpfile="tmp.catalog"
catalog="catalog.dat"
stationfile = "STATIONS.sta"
#tmpstations = "STATIONS.xml"
out = open(catalog,"w")
#tmp_stations = open(tmpstations,"wb")
fstations = open(stationfile,"w")
client = Client("IRIS")


cat = client.get_events(starttime=starttime,endtime=endtime,mindepth=mindepth,maxdepth=maxdepth,minmagnitude=minmagnitude,maxmagnitude=maxmagnitude,orderby="magnitude")
cat.write(tmpfile,format="CNV")

stations={}
with open(tmpfile,"r") as events:
        for event in events:
            if(event != "\n"):
                year, month, day, hour, minutes, sec, msec, evla, evlo, evdp, evmag = parse_event(event)
                tb = UTCDateTime(year+"-"+month+"-"+day+"T"+hour+":"+minutes+":"+sec+"."+msec)-10
                te = UTCDateTime(year+"-"+month+"-"+day+"T"+hour+":"+minutes+":"+sec+"."+msec)+300
                #nearby_stations = client.get_stations(network="*", sta="*",starttime=tb,endtime=te,latitude=evla,longitude=evlo,minradius=minradius,maxradius=maxradius, level= 'channel')
                try:
                    nearby_stations = client.get_stations(network="*", sta="*",starttime=tb,endtime=te,latitude=evla,longitude=evlo,minradius=minradius,maxradius=maxradius, level= 'channel')
                    #nearby_stations.write(tmp_stations, format="STATIONXML")
                    n_stations=0
                    networks=set()
                    while True:
                        network = random.choice(nearby_stations)
                        networks.add(network.code)
                        shuffled_stations = random.sample(network.stations, len(network))
                        #print(shuffled_stations)
                        for station in shuffled_stations:
                            station_code = station.code
                            if station.code not in stations.keys():
                                n_stations+=1
                                stations[station_code]={}
                                stations[station_code]['network'] = network.code
                                stations[station_code]['channels'] = set()
                                stations[station_code]['longitude'] = station.longitude
                                stations[station_code]['latitude'] = station.latitude
                                stations[station_code]['elevation'] = station.elevation
                            cont=0
                            for chan in station:
                                if chan.sample_rate >= 100.0: # Sample rate necesario para conseguir espectrogramas de calidad
                                    stations[station.code]['channels'].add(chan.code)
                                    cont+=1
                            if cont == 0:
                                stations.pop(station.code)
                                n_stations-=1
                        if n_stations >= max_sta or len(networks) == len(nearby_stations):
                                break
                        
                except obspy.clients.fdsn.header.FDSNNoDataException:
                    print("No stations nearby")
                    continue

for station_code in stations.keys():
    fstations.write('{} {} {} {} {} {}\n'.format(stations[station_code]['longitude'], stations[station_code]['latitude'], stations[station_code]['network'], station_code, '.'.join(stations[station_code]['channels']), stations[station_code]['elevation']))

fstations.close()
