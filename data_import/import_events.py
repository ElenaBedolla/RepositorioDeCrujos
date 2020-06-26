import mysql.connector
import datetime
import os

mydb = mysql.connector.connect(
  host="localhost",
  database="Sismos",
  user="root"
)

cursor = mydb.cursor()

add_event = ("INSERT INTO EARTHQUAKE(id, date_time, latitude, longitude, depth,magnitude) VALUES (%s,%s, %s, %s, %s,%s)")

cur_path = os.path.dirname(__file__)
filename = os.path.join(cur_path, '../catalog.dat')

f = open(filename, 'r')
for i, line in enumerate(f):
    event = line.split()
    time_str = event[0]
    time_parse = list(map(int, [time_str[:4], time_str[4:6], time_str[6:8], time_str[8:10], time_str[10:12], time_str[12:14], time_str[-2:]]))
    time_parse[-1]*=10
    time = datetime.datetime(*time_parse)
    event = (i+1,time.strftime('%Y-%m-%d %H:%M:%S.%f'), event[1], event[2],event[3],event[4])
    cursor.execute(add_event, event)
    
mydb.commit()

cursor.close()
mydb.close()
              
