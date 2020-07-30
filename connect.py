import mysql.connector
import json
import paramiko
from scp import SCPClient
import os
import mysql.connector

def load_credentials(cur_path, rel_cred_file):
    credentials_file = os.path.join(cur_path, rel_cred_file)
    with open(credentials_file) as f:
        credentials = json.loads(f.read())
    #print(credentials[0])
    return credentials

def connect_db(cur_path, rel_cred_file):
    credentials=load_credentials(cur_path, rel_cred_file)
    mydb = mysql.connector.connect(**credentials["MySQL"])
    
    return mydb

def connect_SCP(cur_path, rel_cred_file):
    credentials_file = os.path.join(cur_path, rel_cred_file)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    credentials=load_credentials(cur_path, credentials_file)
    client.connect(**credentials["SSH"])
    scp = SCPClient(client.get_transport())
    return scp

if __name__ == "__main__":
    cur_path = os.path.dirname(__file__)
    mysql_creds = load_credentials(cur_path, "credentials.json")["MySQL"]
    print(mysql_creds["database"], mysql_creds["user"], mysql_creds["password"])
