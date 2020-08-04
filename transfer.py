from . import connect_SCP
import os

cur_path = os.path.dirname(__file__)
ssh, scp = connect_SCP(cur_path, "credentials.json")
sql = os.path.join(cur_path, "db_def/Sismos_backup.sql")
scp.put(sql, "~/RepositorioDeCrujos/db_def")

ssh.exec_command('rm -R ~/RepositorioDeCrujos/Template')
template = os.path.join(cur_path, "Template")
scp.put(template, "~/RepositorioDeCrujos", recursive=True)

map_html = os.path.join(cur_path, "website/map.html")
scp.put(map_html, "~/RepositorioDeCrujos/website")
