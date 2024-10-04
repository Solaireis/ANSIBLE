#!/bin/bash
DATES=$(date +%Y-%m-%d_%H-%M-%S)
echo $DATES 
scp /etc/bind/named.conf.slave root@10.22.0.1:/root/backups/slave/$DATES\_$HOSTNAME.tar.gz
scp /etc/bind/named.conf root@10.22.0.1:/root/backups/slave/$DATES\_$HOSTNAME.tar.gz