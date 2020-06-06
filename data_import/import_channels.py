import mysql.connector
import os

mydb = mysql.connector.connect(
  host="localhost",
  database="Sismos",
  user="root"
)
cursor = mydb.cursor()
add_channel = ("INSERT INTO CHANNEL(symbol, station) VALUES (%s, %s)")

cur_path = os.path.dirname(__file__)
filename = os.path.join(cur_path, '../STATIONS.sta')

f = open(filename, 'r')
for line in f:
    station = line.split()
    channels = station[4].split('.')
    for chan in channels:
        cursor.execute(add_channel, (chan,station[3]))
    
mydb.commit()

cursor.close()
mydb.close()
