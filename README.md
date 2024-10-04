# ANSIBLE

<p>If using this repository for learning use, please cite this repository as origin </p>
<p> Thank you! </p>


## Credits
- Yong En - Initial Linux playbooks & whole Python Programmability section

- Lecturers - for Guidance and support


## NOTE:
WorldSkills Solution for Skill39 ITNSA WSC 2022 SE 

This is for self learning and education purposes, not for commercial use.
Password use here are for learning purposes and are not indicative of actual real world machines

Unarchived my optimised version, as i withdrawn from 2024 lyon ITNSA, these were my solution when i was in a proper mental health.

### How to Install
```bash
aptitude install ansible


# Make the hostfile directory
mkdir /etc/ansible/
vi hosts


# Add the  Playbooks
mkdir -p /data/ansible/linux
vi 1-hostname.yml


# to run the playbooks

ansible-playbook 1-hostname.yml

# to read docs
ansible-doc

```
You may refer to redhat for better documentation
