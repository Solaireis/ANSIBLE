# ANSIBLE
## NOTE:
This is for self learning and education purposes, not for commercial use.
Password use here are for learning purposes and are not indicative of actual real world machines

The Config here is outdated, optimised versions of my playbooks are privated for competition reasons
Hence im unlocking this repository


## What is Ansible?
Ansible is a configuration management tool, it is used to automate the configuration of machines.
## How does it work?
Ansible uses SSH to connect to machines and run commands on them.
## How to install Ansible?
### On Ubuntu
```
sudo apt-get update
sudo apt-get install software-properties-common
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible
```
### On Mac
```
brew install ansible
```
## How to use Ansible?
### Ansible commands
```
ansible --version
ansible-playbook playbook.yml
```

## Automation play book scripts
Runs on python modules, used to automate machines to do stuffs
jinja2 syntax to check on variables
