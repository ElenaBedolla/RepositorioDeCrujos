import mysql.connector
import os
import re
from .. import connect_db

cur_path = os.path.dirname(__file__)
mydb = connect_db(cur_path, "../credentials.json")
cursor = mydb.cursor()
add_channel = ("INSERT INTO CHANNEL(symbol, station) VALUES (%s, %s)")

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
