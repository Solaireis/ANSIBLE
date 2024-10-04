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

as i withdrawn from 2024 lyon ITNSA in march 2024 & that the WSC2024 round has concluded.
i have unarchived my optimised version.
these were my solution when i was in a proper mental health training for lyon 2024 in 2023 and early 2024.


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
