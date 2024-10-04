#!/bin/sh
dig @192.168.0.3 wss2023-linuxhost-001.wss2023.com +noall +answer
dig @192.168.0.10 wss2023-linuxhost-002.wss2023.com +noall +answer
dig @192.168.0.3 wss2023-linuxhost-003.wss2023.com +noall +answer
dig @192.168.0.10 wss2023-rtr1.wss2023.com +noall +answer
dig @192.168.0.3 wss2023-rtr2.wss2023.com +noall +answer 
dig @192.168.0.10 wss2023-rtr3.wss2023.com +noall +answer
dig @192.168.0.3 wss2023-rtr4.wss2023.com +noall +answer
dig @192.168.0.10 wss2023-dc-001.wss2023.com +noall +answer
dig @192.168.0.3 wss2023-host-002.wss2023.com +noall +answer
dig @192.168.0.10 wss2023-host-003.wss2023.com +noall +answer
dig @192.168.0.3  intranet.wss2023.com +noall +answer
