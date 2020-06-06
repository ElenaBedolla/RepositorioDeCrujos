from obspy.clients.fdsn import Client
from obspy import UTCDateTime, read
import mysql.connector
import os
import json
import datetime
import shutil

mydb = mysql.connector.connect(
  host="localhost",
  database="Sismos",
  user="root"
)

cursor = mydb.cursor()

# Borrar registros viejos

delete_previous =("DELETE FROM CHANNEL_EARTHQUAKE")

cursor.execute(delete_previous)


delete_previous =("DELETE FROM EARTHQUAKE")

cursor.execute(delete_previous)

# Registrar los nuevos sismos

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

# Registrar los nuevos sismogramas por cada canal

add_channel_earthquake = ("INSERT INTO CHANNEL_EARTHQUAKE(station, channel, earthquake_id, sample_rate, waveform, start_time, end_time) VALUES (%s, %s, %s, %s, %s, %s, %s)")

cur_path = os.path.dirname(__file__)
main_folder = os.path.join(cur_path, '../Template')


event_folders = os.listdir(main_folder)
for event_folder in event_folders:
    event_data = event_folder.split('-')
    event_path = os.path.join(main_folder, event_folder)
    files = os.listdir(event_path)
    for file in files:
        file_path = os.path.join(event_path, file)
        st = read(file_path)
        trace = list(map(float, list(st[0].data)))
        waveform = json.dumps(trace)
        sample_rate = st[0].stats.sampling_rate
        start_time = st[0].stats.starttime.strftime('%Y-%m-%d %H:%M:%S.%f')
        end_time = st[0].stats.endtime.strftime('%Y-%m-%d %H:%M:%S.%f')
        file_symbols = file.split('.')
        final_channel_earthquake = (file_symbols[1], file_symbols[2], event_data[-1], sample_rate, waveform, start_time, end_time)
        cursor.execute(add_channel_earthquake, final_channel_earthquake)

mydb.commit()
cursor.close()
mydb.close()

shutil.rmtree(main_folder)
