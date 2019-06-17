import csv
import matplotlib.pyplot as plt
import numpy as np
import datetime
 
EXCL_dict = []
FREN_dict = []
TLKM_dict = []
ISAT_dict = []
with open('EXCL.JK.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        EXCL_dict.append({'Date':row['Date'],'Open':row['Open'],'High':row['High'],'Low':row['Low'],'Close':row['Close'],'Adj Close':row['Adj Close'],'Volume':row['Volume']})
with open('FREN.JK.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        FREN_dict.append({'Date':row['Date'],'Open':row['Open'],'High':row['High'],'Low':row['Low'],'Close':row['Close'],'Adj Close':row['Adj Close'],'Volume':row['Volume']})
with open('TLKM.JK.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        TLKM_dict.append({'Date':row['Date'],'Open':row['Open'],'High':row['High'],'Low':row['Low'],'Close':row['Close'],'Adj Close':row['Adj Close'],'Volume':row['Volume']})
with open('ISAT.JK.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        ISAT_dict.append({'Date':row['Date'],'Open':row['Open'],'High':row['High'],'Low':row['Low'],'Close':row['Close'],'Adj Close':row['Adj Close'],'Volume':row['Volume']})
print("Reading Complete!")
EXCL=[int(float(x['Close'])) for x in EXCL_dict]
FREN=[int(float(x['Close'])) for x in FREN_dict]
TLKM=[int(float(x['Close'])) for x in TLKM_dict]
ISAT=[int(float(x['Close'])) for x in ISAT_dict]
dates = [datetime.datetime.strptime(x['Date'], "%Y-%m-%d").strftime("%d-%m-%Y") for x in EXCL_dict]
print(EXCL)
print(FREN)
print(TLKM)
print(ISAT)

index = np.arange(len(dates))
a=plt.plot(dates, EXCL, 'g')
b=plt.plot(dates, FREN, 'b')
c=plt.plot(dates, TLKM, 'r')
d=plt.plot(dates, ISAT, 'y')
plt.xlabel('Tanggal', fontsize=15)
plt.ylabel('Rupiah (IDR)', fontsize=15)
plt.xticks(index, dates, fontsize=7, rotation=30)
plt.title('Harga Historis Saham Provider Telco Indonesia')
plt.locator_params(axis='x', nbins=20)
#plt.legend((a, b, c, d), ('PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Telekomunikasi Idonesia Tbk','PT Indosar Tbk'))
plt.show()

