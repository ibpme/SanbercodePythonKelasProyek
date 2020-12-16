from openpyxl import Workbook 
from openpyxl.chart import BarChart ,Reference
import pandas as pd 

data_jumlah_penduduk  = pd.read_csv("./jumlah-penduduk-kota-bandung.csv",sep=',')
data_luas_wilayah = pd.read_csv("./luas-wilayah-menurut-kecamatan-di-kota-bandung-2017.csv",sep=',')

def match_string(string1,string2):
    if(string1.lower().replace(" ","")==string2.lower().replace(" ","")):
        return True
    else :
        return False

def cari_jumlah_penduduk(nama_wilayah):
    for kecamatan,jumlah_penduduk in zip(data_jumlah_penduduk['Kecamatan  '],data_jumlah_penduduk['Jumlah_Penduduk']):
        match = match_string(str(kecamatan),str(nama_wilayah))
        if match:
            return int(jumlah_penduduk)
        else: 
            continue
    return None

wb = Workbook()
ws = wb.active
ws.title = "Kepadatan Penduduk"
ws.append(["Nama Kecamatan","Kepadatan Penduduk"])

data_luas_wilayah = zip(data_luas_wilayah['Nama Kecamatan'],data_luas_wilayah['Luas Wilayah (m2)'])

index = 0
for wilayah,luas_wilayah in data_luas_wilayah:
    jumlah_penduduk = cari_jumlah_penduduk(wilayah)
    if jumlah_penduduk == None:
        continue
    ws.append([wilayah,jumlah_penduduk*100/luas_wilayah])
    index +=1

chart1 = BarChart()
chart1.type = "col"
chart1.style = 3
chart1.title = "Bar Chart"
chart1.y_axis.title = 'Kepadatan Penduduk per 100m2'
chart1.x_axis.title = 'Kecamatan'

data = Reference(ws, min_col=2, min_row=1, max_row=index,)
cats = Reference(ws, min_col=1, min_row=1, max_row=index)
chart1.height = 10 # default is 7.5
chart1.width = 30 # default is 15
chart1.add_data(data, titles_from_data=True)
chart1.set_categories(cats)
ws.add_chart(chart1, "G2")

wb.save("Iman-BudiPranakasih.xlsx")

