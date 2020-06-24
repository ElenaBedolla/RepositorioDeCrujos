from obspy.clients.fdsn import Client
from obspy import UTCDateTime, read
import os
import datetime
import copy

end_time = datetime.datetime.now() 
start_time = end_time-datetime.timedelta(hours=24) # Intervalo de busqueda desde 12 horas anteriores a la actual
starttime = UTCDateTime(start_time.isoformat())
print(start_time.isoformat())
endtime = UTCDateTime(end_time.isoformat())

latitude=15
longitude=-90
minradius=0
maxradius=1

stationfile = "STATIONS.sta"
tmpstations = "STATIONS.xml"
tmp_stations = open(tmpstations,"wb")
fstations = open(stationfile,"w")
client = Client("IRIS")

nearby_stations = client.get_stations(starttime=starttime,endtime=endtime,latitude=latitude,longitude=longitude,minradius=minradius,maxradius=maxradius, level= 'channel')
nearby_stations.write(tmp_stations, format="STATIONXML")

tmp_stations.close()

stations={}
for network in nearby_stations:
    for station in network:
            station_code = station.code
            if station.code not in stations.keys():
                stations[station_code]={}
                stations[station_code]['network'] = network.code
                stations[station_code]['channels'] = set()
                stations[station_code]['longitude'] = station.longitude
                stations[station_code]['latitude'] = station.latitude
                stations[station_code]['elevation'] = station.elevation
            for chan in station:
                if chan.sample_rate >= 100.0: # Sample rate necesario para conseguir espectrogramas de calidad
            	    stations[station.code]['channels'].add(chan.code)

for station_code in stations.keys():
    fstations.write('{} {} {} {} {} {}\n'.format(stations[station_code]['longitude'], stations[station_code]['latitude'], stations[station_code]['network'], station_code, '.'.join(stations[station_code]['channels']), stations[station_code]['elevation']))

fstations.close()
