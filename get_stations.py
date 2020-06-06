from obspy.clients.fdsn import Client
from obspy import UTCDateTime, read
import os
import datetime
import copy
from bs4 import BeautifulSoup as Soup

end_time = datetime.datetime.now() 
start_time = end_time-datetime.timedelta(hours=24) # Intervalo de busqueda desde 12 horas anteriores a la actual
starttime = UTCDateTime(start_time.isoformat())
print(start_time.isoformat())
endtime = UTCDateTime(end_time.isoformat())

latitude=15
longitude=-90
minradius=0
maxradius=20

stationfile = "STATIONS.sta"
tmpstations = "STATIONS.xml"
tmp_stations = open(tmpstations,"w")
stations = open(stationfile,"w")

client = Client("SCEDC")

nearby_stations = client.get_stations(starttime=starttime,endtime=endtime,latitude=latitude,longitude=longitude,minradius=minradius,maxradius=maxradius, level= 'channel')
nearby_stations.write(tmp_stations, format="STATIONXML")

tmp_stations.close()

for network in nearby_stations:
    for station in network:
        channels = set()
        for chan in station:
            channels.add(chan.code)
        stations.write('{} {} {} {} {} {}\n'.format(station.longitude, station.latitude, network.code, station.code, '.'.join(channels), station.elevation))

stations.close()
