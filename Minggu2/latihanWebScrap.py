from urllib.request import urlopen
from bs4 import BeautifulSoup

alamat = "https://blog.sanbercode.com/"
html = urlopen(alamat)
data = BeautifulSoup(html, 'html.parser')

items = data.findAll("a", {"class":"text-dark"})
print(items,len(items))