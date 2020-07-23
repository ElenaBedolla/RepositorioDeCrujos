import folium
import os
from events import parse_event
import json

eventfile = "tmp.catalog"
with open(eventfile, "r") as f:
    events=[]
    for event in f:
        if event!= '\n':
            events.append(list(parse_event(event)))

events_t = list(zip(*events))
evlas = list(map(float, events_t[7]))
evlos = list(map(float, events_t[8]))
max_evla = max(evlas)
min_evla = min(evlas)
max_evlo = max(evlos)
min_evlo = min(evlos)

mean_evla = sum(evlas)/len(evlas)
mean_evlo = sum(evlos)/len(evlos)
        
m = folium.Map(location=[mean_evla, mean_evlo])


for i, event in enumerate(events):
    html = '''Magnitud: %s<br>
              Dia: %s/%s<br>
              Tiempo: %s:%s:%s.%s<br>
              Profundidad: %s<br>
              Coordenadas: %s, %s<br>
              <form method="post" action="index.php" target="_parent">
                  <button type="submit" name="earthquake" value="[%s, %s]">X</button>
                  <!--
                  if(!empty($_POST['earthquake_id']))
                  {
                      $_SESSION['earthquake_id'] = $_POST['earthquake_id'];
                  }
                  -->
              </form>
              '''%(event[10], event[2], event[1], event[3], event[4], event[5], event[6], event[9], event[7], event[8], i+1, event[0]+event[1]+event[2]+event[3]+event[4]+event[5])

    #iframe = folium.IFrame(html, width=100, height=100)

    #popup = folium.Popup(iframe, max_width=100)	
    folium.Marker([event[7], event[8]], popup=html).add_to(m)


m.fit_bounds([[min_evla, min_evlo], [max_evla, max_evlo]])
m.save(outfile= "website/map.html")

