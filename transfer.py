from . import connect_SCP
import os

cur_path = os.path.dirname(__file__)
scp = connect_SCP(cur_path, "credentials.json")
sql = os.path.join(cur_path, "db_def/Sismos_backup.sql")
scp.put(sql, "~/RepositorioDeCrujos/db_def")

template = os.path.join(cur_path, "Template")
scp.put(template, "~/RepositorioDeCrujos", recursive=True)
