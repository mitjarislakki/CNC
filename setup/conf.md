### ORANGE
`sudo ./server.sh enx000acd2c2a17 169.254.9.14 24`
### GRAY
`sudo ./server.sh enx000acd2c2a16 169.254.9.14 24`
### RED
`sudo ./client.sh enxa0cec887759a 169.254.9.12 169.254.9.14 24 c1`
### GRAY
`sudo ./client.sh enxa0cec8877051 169.254.9.11 169.254.9.13 24 c2`

`sudo lshw -c network | grep "logical name:" | sed 's/^.*: //' | while read line ; do ifconfig "$line" up ; done`