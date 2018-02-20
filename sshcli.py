import paramiko
import sys

try:
	user = sys.argv[1]
	host = sys.argv[2]
	passwd = sys.argv[3]
except:
	print 'Usage: python sshcli.py <user> <host> <password>'
	print
	print 'Usage: ./sshcli.py <user> <host> <password>'
	sys.exit(1)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)

while True:
    	comando = raw_input('Code: ')
    	entrada, saida, erros = client.exec_command(comando)
    	print saida.readlines()
