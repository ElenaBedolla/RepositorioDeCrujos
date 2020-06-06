if [ $1 == 'setup' ];
then
    if [[ ! -z "`/opt/lampp/bin/mysql -u root "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME='db'" 2>&1`" ]];
    then
        /opt/lampp/bin/mysql -u root -e "DROP DATABASE Sismos"       
    fi
    /opt/lampp/bin/mysql -u root -e "CREATE DATABASE Sismos"    
    /opt/lampp/bin/mysql -u root Sismos < db_def/Sismos.sql
    python data_import/import_stations.py
    python data_import/import_channels.py
    python template_download.py
    python data_import/update_earthquakes.py
elif [ $1 == 'update' ]
then
    python template_download.py
    python data_import/update_earthquakes.py
fi
/opt/lampp/bin/mysql -u root -D Sismos -e "SELECT * FROM EARTHQUAKE"
