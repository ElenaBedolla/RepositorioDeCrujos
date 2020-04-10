import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  database="Sismos",
  user="root"
)
cursor = mydb.cursor()
add_station = ("INSERT INTO STATION(symbol, latitude, longitude, elevation) VALUES (%s, %s, %s, %s)")

f = open("./IRIS.sta", 'r')
for line in f:
    station = line.split()
    station = (station[3], station[1], station[0], station[5])
    cursor.execute(add_station, station)
    
mydb.commit()

cursor.close()
mydb.close()
              
