if [ $1 == 'processor' ];
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
    cd ..
    python -m RepositorioDeCrujos.data_import.import_stations
    python -m RepositorioDeCrujos.data_import.import_channels
    python -m RepositorioDeCrujos.data_import.update_earthquakes
    python -m RepositorioDeCrujos.spectrograms
    python -m RepositorioDeCrujos.map
    /opt/lampp/bin/mysql -u root Sismos > RepositorioDeCrujos/db_def/Sismos_backup.sql
    python -m RepositorioDeCrujos.transfer
    cd RepositorioDeCrujos
elif [ $1 == 'server' ]
then
    mysql_creds=$(python connect.py)
    mysql_split=(${mysql_creds})
    echo ${mysql_split[0]}
    mysql -u ${mysql_split[1]} -p${mysql_split[2]} ${mysql_split[0]} < db_def/Sismos_backup.sql
fi
/opt/lampp/bin/mysql -u root -D Sismos -e "SELECT * FROM EARTHQUAKE"
