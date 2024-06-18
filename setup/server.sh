#!/bin/sh

ip addr flush flush dev eno1
ip addr add 169.254.9.15/24 dev eno1
ip link set eno1 up
iperf3 -s