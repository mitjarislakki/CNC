#!/bin/sh

INTERF=enxb88d1254d259
SRC=169.254.9.17
DST=169.254.9.15

ip netns add c0
ip link set $INTERF netns c0

ip netns exec c0 ip addr add dev $INTERF $SRC/24
ip netns exec c0 ip link set dev $INTERF up
ip netns exec c0 iperf3 -c $DST -B $SRC > output.txt

ip netns del c0