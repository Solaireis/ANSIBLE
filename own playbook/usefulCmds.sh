#!/bin/bash

#kms
ansible -m debug -a var=hostname,ansible_host all | grep ' \: .* ' > records.txt

#then use the following ouput to construct the master record