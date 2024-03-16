import winrm

session = winrm.Session("192.168.1.2", auth=("winrm13910", "zaq1xsw2"))

result = session.run_cmd('ipconfig', ['/all'])

print(result.std_out)

print(result.std_err)





