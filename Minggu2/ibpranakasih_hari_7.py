from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def kompas():
    alamat = "https://kompas.com/"
    html = urlopen(alamat)
    data = BeautifulSoup(html, 'html.parser')

    items = data.findAll("h4", {"class":"most__title"})
    judul_populer = []
    for item in items:
        content = item.contents
        judul_populer.append(content[0])
    judul_populer_df = pd.DataFrame({"Judul Berita Populer":judul_populer})
    print(judul_populer_df)

kompas()