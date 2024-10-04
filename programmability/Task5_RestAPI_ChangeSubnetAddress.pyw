import requests

url = 'http://192.168.0.253:8697/api/vmnets'
myobj = {"name":"vmnet9", "type":"hostOnly","dhcp":"false","subnet":"192.168.0.0","mask":"255.255.255.0"}


x = requests.post(url, json=myobj,auth=('admin','P@ssw0rd'), headers={'Content-Type': 'application/vnd.vmware.vmw.rest-v1+json','Accept':'application/vnd.vmware.vmw.rest-v1+json'} ,verify=False)

print(x.text)

# y = requests.get(url,auth=('admin','P@ssw0rd'))

# print(y.text)
