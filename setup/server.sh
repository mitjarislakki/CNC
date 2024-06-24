#!/bin/sh
INTERF="$1"
SRC="$2"
MASK="$3"

ip addr flush dev $INTERF
ip addr add dev $INTERF $SRC/$MASK
ip link set dev $INTERF up

iperf3 -s -B $SRC

