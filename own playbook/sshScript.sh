#!/bin/bash

#copy all ssh keys to the remote linux machines
ssh-copy-id root@10.22.0.1 | echo "P@ssw0rd" 
ssh-copy-id root@10.22.0.2 | echo "P@ssw0rd" 
ssh-copy-id root@10.22.0.3 | echo "P@ssw0rd" 
ssh-copy-id root@10.22.0.4 | echo "P@ssw0rd" 
ssh-copy-id root@10.22.0.5 | echo "P@ssw0rd" 