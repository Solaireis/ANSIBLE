#!/bin/bash

#kms
ansible -m debug -a var=hostname,ansible_host all | grep ' \: .* ' > records.txt
