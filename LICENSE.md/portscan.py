import socket
import sys
import time

print '_____________________________________'
print '               WELCOME               '
print '_____________ Port Scan _____________'
print '  https://github.com/pentesterjeff   '
print '________________ v2 _________________'
print

try:
        url = sys.argv[1]
        ports = [20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 123, 143, 156, 179, 442, 1723, 1863, 3128, 2289]
except:
        print 'Usege: python portscan.py <url>'
        print
        print 'Usage: ./portscan.py'
        sys.exit()

print '      Please wait for loading...     '
print '_____________________________________'
print
for port in ports:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.settimeout(0.5)
        code = c.connect_ex((url, port))
        time.sleep(1)
        if code == 0:
                print str(port) + "-> OPEN"
                print

time.sleep(2)
print 'Scan Completed...'
