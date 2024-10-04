from paramiko import *
import paramiko
from scp import SCPClient
import time



command1 = "mkdir -p /etc/ansible/cisco/group_vars/"
command2 = "mkdir -p /etc/ansible/credentials/"
command3 = "mkdir -p /data/ansible/windows/2"
command4 = "mkdir -p /data/ansible/windows/3"
command5 = "mkdir -p /data/ansible/windows/6"
command6 = "mkdir -p /etc/ansible/group_vars/"


host = "192.168.0.50"
username = "root"
password = "P@ssw0rd"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


client.connect(host, username=username, password=password)
_stdin,_stdout,_stderr = client.exec_command(command1)
print(_stdout.read().decode())
client.close()

time.sleep(5)

client.connect(host, username=username, password=password)
_stdin,_stdout,_stderr = client.exec_command(command2)
client.exec_command(command3)
client.exec_command(command4)
client.exec_command(command5)
print(_stdout.read().decode())
client.close()

time.sleep(5)

################################################################
client.connect(host, username=username, password=password)

with SCPClient(client.get_transport()) as scp:
    scp.put('C:\\FYPJ_8_sysprep.yml', '/data/ansible/.')
    scp.put('C:\\unattend.xml', '/data/ansible/.')
    scp.put('C:\\PsGetsid.exe', '/root/.')
    scp.put('C:\\windows_playbook\\windows',recursive=True,remote_path='/data/ansible/')
    scp.put('C:\\linux_playbook\\linux',recursive=True,remote_path='/data/ansible/')
    scp.put('C:\\cisco_playbook\\cisco',recursive=True,remote_path='/data/ansible/')

    scp.put('C:\\ansible',recursive=True,remote_path='/etc/')

     




client.close()

exit()