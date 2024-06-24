import subprocess
import time

terminal_cmd = "gnome-terminal -- bash -c 'sudo bash {} ; exec bash'"

servers = ["./server.sh enx000acd2c2a17 169.254.9.14 24",
           "./server.sh enx000acd2c2a16 169.254.9.13 24"
           ]

clients = ["./client.sh enxa0cec887759a 169.254.9.12 169.254.9.14 24 c1",
           "./client.sh enxa0cec8877051 169.254.9.11 169.254.9.13 24 c2"
           ]

processes = []

for server in servers:
    cmd = terminal_cmd.format(server)
    process = subprocess.Popen(cmd, shell=True)
    processes.append(process)

time.sleep(2)

for client in clients:
    cmd = terminal_cmd.format(client)
    process = subprocess.Popen(cmd, shell=True)
    processes.append(process)

for p in processes:
    p.wait()