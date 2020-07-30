import mysql.connector
import os
import re
from .. import connect_db

cur_path = os.path.dirname(__file__)
mydb = connect_db(cur_path, "../credentials.json")


cursor = mydb.cursor()
add_station = ("INSERT INTO STATION(symbol, latitude, longitude, elevation) VALUES (%s, %s, %s, %s)")

filename = os.path.join(cur_path, '../STATIONS.sta')

f = open(filename, 'r')
for line in f:
    station = line.split()
    station = (station[3], station[1], station[0], station[5])
    cursor.execute(add_station, station)
    
mydb.commit()

cursor.close()
mydb.close()
              
