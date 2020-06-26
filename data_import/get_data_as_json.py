from obspy.clients.fdsn import Client
from obspy import UTCDateTime, read
import os
import json

main_folder='./Template/'
event_folders = os.listdir(main_folder)
JSON_trace_folder = './JSON_trace_data/'
for event_folder in event_folders:
    files = os.listdir(main_folder+event_folder)
    for file in files:
        st = read(main_folder+event_folder+'/'+file)
        trace = list(map(float, list(st[0].data)))
        #json_trace = json.dumps(trace)
        f = open(main_folder+event_folder+'/'+file+'.json', 'w')
        json.dump(trace, f)
