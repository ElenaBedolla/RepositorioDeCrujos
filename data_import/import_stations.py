import mysql.connector
import os

mydb = mysql.connector.connect(
  host="localhost",
  database="Sismos",
  user="root"
)
cursor = mydb.cursor()
add_station = ("INSERT INTO STATION(symbol, latitude, longitude, elevation) VALUES (%s, %s, %s, %s)")

cur_path = os.path.dirname(__file__)
filename = os.path.join(cur_path, '../STATIONS.sta')

f = open(filename, 'r')
for line in f:
    station = line.split()
    station = (station[3], station[1], station[0], station[5])
    cursor.execute(add_station, station)
    
mydb.commit()

cursor.close()
mydb.close()
              
