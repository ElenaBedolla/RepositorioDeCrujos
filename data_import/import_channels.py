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
filename = os.path.join(cur_path, '../IRIS.sta')

chans = ['E', 'N', 'Z']

f = open(filename, 'r')
for line in f:
    station = line.split()
    channel = station[4]
    for chan in chans:
        final_chan = (channel[:2]+chan, station[3])
        cursor.execute(add_channel, final_chan)
    
mydb.commit()

cursor.close()
mydb.close()
