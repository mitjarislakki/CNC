#!/bin/sh

INTERF="$1"
SRC="$2"
DST="$3"


ip netns add c0
ip link set $INTERF netns c0

ip netns exec c0 ip addr add dev $INTERF $SRC/24
ip netns exec c0 ip link set dev $INTERF up
ip netns exec c0 iperf3 -c $DST -B $SRC

ip netns del c0