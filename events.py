import re

def parse_event(event):
    event = event.strip("\n")
    ymd, hm, s, lat, lon , dep, mag, jk = event.split() # Datos del evento (sismo)
    year="20"+ymd[:2]
    month=ymd[2:4]
    day=ymd[4:6]
    hour=hm[:2]
    minutes=hm[2:4]
    sec,msec=s.split(".")
    if (len(sec)<2):
        sec="0"+sec
        # Eliminar letras en caso de que aparezcan
    evla=re.sub('[A-Za-z]', '', lat[:7]) # Latitud
    evlo=re.sub('[A-Za-z]', '', lon[:8]) # Longitud
    evdp=dep # Profundidad [km]
    evmag=mag # Magnitud sismica en escala Richter
    return year, month, day, hour, minutes, sec, msec, evla, evlo, evdp, evmag
