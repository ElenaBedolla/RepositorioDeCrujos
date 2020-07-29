if [ $1 == 'setup' ];
then
    rm -R Template
    if [[ ! -z "`/opt/lampp/bin/mysql -u root "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME='Sismos'" 2>&1`" ]];
    then
        /opt/lampp/bin/mysql -u root -e "DROP DATABASE Sismos" 
        echo Deleted previous database      
    fi
    /opt/lampp/bin/mysql -u root -e "CREATE DATABASE Sismos"    
    /opt/lampp/bin/mysql -u root Sismos < db_def/Sismos.sql
    python get_event_stations.py
    python waveform_download.py
    python data_import/import_stations.py
    python data_import/import_channels.py
    cd ..
    python -m RepositorioDeCrujos.data_import.update_earthquakes
    cd RepositorioDeCrujos
    python spectrograms.py
    python map.py
elif [ $1 == 'update' ]
then
    rm -R Template
    python get_event_stations.py
    python waveform_download.py
    python data_import/update_earthquakes.py
    python spectrograms.py
    python map.py
fi
/opt/lampp/bin/mysql -u root -D Sismos -e "SELECT * FROM EARTHQUAKE"
