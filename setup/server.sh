#!/bin/sh
SRC="$1"

ip addr flush dev eno1
ip addr add $SRC/24 dev eno1
ip link set eno1 up
iperf3 -s