/opt/lampp/bin/mysql -u root -e "CREATE DATABASE Sismos"
/opt/lampp/bin/mysql -u root -e Sismos < db_def/Sismos.sql

python template_download.py
python data_import/import_stations.py
python data_import/import_channels.py
python data_import/update_earthquakes.py

/opt/lampp/bin/mysql -u root -DSismos -e "SELECT * FROM EARTHQUAKE"
