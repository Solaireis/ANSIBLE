#!/bin/bash
DATES=$(date +%Y-%m-%d_%H-%M-%S)
echo $DATES 
scp /etc/bind/applix.com.lan root@10.22.0.1:/root/backups/master/$DATES\_$HOSTNAME.tar.gz
