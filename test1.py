import winrm

host = "192.168.1.2"
username = "winrm13910"
password = "zaq1xsw2"
session = winrm.Session(host, auth=(username, password))

result = session.run_cmd('ipconfig', ['/all'])






