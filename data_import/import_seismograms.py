import mysql.connector
import os
import json

mydb = mysql.connector.connect(
  host="localhost",
  database="Sismos",
  user="root"
)
cursor = mydb.cursor()
add_channel_earthquake = ("INSERT INTO CHANNEL_EVENT(station, channel, event_id, sample_rate, waveform, start_time, end_time) VALUES (%s, %s, %s, %s, %s, %s, %s)")

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
        #json_trace = json.dumps(trace)
        waveform = json.dumps(trace)
        sample_rate = st[0].stats.sampling_rate
        start_time = st[0].stats.startime.split('T')
        end_time = st[0].stats.endtime.split('T')
        file_symbols = file.split('.')
        final_channel_earthquake = (file_symbols[1], file_symbols[2], event_data[-1], sample_rate, waveform, start_time[0]+startime[1][:-1], end_time+endtime[1][:-1])
        cursor.execute(add_channel_earthquake, final_channel_earthquake)

mydb.commit()

cursor.close()
mydb.close()
