import subprocess as sp

CLIENT_INTERF = 'enxb88d1254d259'
CLIENT_IP = '169.254.9.17'
SERVER_INTERF = 'eno1'
SERVER_IP = '169.254.9.15'
NETMASK = '24'

if __name__ == "__main__":
    f = open('server.txt', 'w')
    c = open('client.txt', 'w')
    server = sp.Popen(['./server.sh', SERVER_INTERF, SERVER_IP, NETMASK], stdout=f, stderr=f)
    
    sp.run(['./client.sh', CLIENT_INTERF, CLIENT_IP, SERVER_IP, NETMASK], stdout=c, stderr=c)

    f.close()
    c.close()
    
    server.terminate()
