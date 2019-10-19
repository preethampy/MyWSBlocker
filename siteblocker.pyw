import time
from datetime import datetime as dt
host = 'C:\Windows\System32\drivers\etc\hosts'
myIp = '103.245.198.110'
websites = ['facebook.com','www.facebook.com','www.instagram.com']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,21):
        with open(host,'r+') as file:
             inside_hosts = file.read()
             print(inside_hosts)
             for website in websites:
                 if website in inside_hosts:
                     pass
                 else:
                     file.write(myIp+" "+website+"\n")
    else:
        with open(host,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for eachline in content:
                if not any(website in eachline for website in websites):
                    file.write(eachline)
            file.truncate()
    break