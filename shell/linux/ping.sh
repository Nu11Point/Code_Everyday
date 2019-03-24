#!/bin/bash
ip="192.168.1.0"
for i in `seq 1 254`
do
	ping -c 2 $ip$i | grep -q 'ttl=' && echo "$ip$i yes" || echo "$ip$i no"
done
