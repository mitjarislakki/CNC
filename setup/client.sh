#!/bin/sh

INTERF="$1"
SRC="$2"
DST="$3"
MASK="$4"
NS="$5"

ip netns add $NS
ip link set $INTERF netns $NS

ip netns exec $NS ip addr add dev $INTERF $SRC/$MASK
ip netns exec $NS ip link set dev $INTERF up
ip netns exec $NS iperf3 -c $DST -B $SRC

ip netns del $NS
