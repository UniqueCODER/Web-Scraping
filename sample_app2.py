
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx =ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link= input('enter -')
count = int(input("count"))
pos = int(input("pos"))

for i in range(0, count):
    html = urllib.request.urlopen(link,context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')

    tags = soup('a')
    c = 0
    p = 0
    for tag in tags:
        p+=1
        if p==pos:
            print(str(tag.get('href',None)))
            link = str(tag.get('href',None))
            p=0
            break
