
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx =ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('enter -')
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('span')
total = 0
for tag in tags:
    #print('Contents:', tag.contents[0])
    total = total+int(tag.contents[0])
print(total)