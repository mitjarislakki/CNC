import subprocess as sp
import time

INTERF='enxb88d1254d259'
SRC='169.254.9.17'
DST='169.254.9.15'

if __name__ == "__main__":
    f = open('server.txt', 'w')
    c = open('client.txt', 'w')
    server = sp.Popen(['./server.sh', DST], stdout=f, stderr=f)
    
    sp.run(['./client.sh', INTERF, SRC, DST], stdout=c, stderr=c)

    f.close()
    c.close()
    
    server.terminate()
