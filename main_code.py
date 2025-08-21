import pandas as pd
url = "https://raw.githubusercontent.com/acookieman/test_assignment/refs/heads/main/train_data.csv"
df = pd.read_csv(url)
print (df.head()) #друк "голови"
print('rows', df.shape[0] ) #кількість рядків
print ('columns', df.shape[1],) #кількість колонок

print (df.dtypes) #вид "типу"

import requests, io
response0 = requests.get(url)
response0.raise_for_status()
is_blank = len(response0.text.strip()) == 0
print(is_blank) #перевірка чи є пусті рядки, якщо нема, то "False"

import requests, io
response1 = requests.get(url)
response1.raise_for_status()
df = pd.read_csv(io.StringIO(response1.text)) 
df[["Quantity", "UnitPrice", "CustomerID"]]
max0=df['Quantity'].max()
min0=df['Quantity'].min()
max1= df['UnitPrice'].max()
min1= df['UnitPrice'].min()
max2= df['CustomerID'].max()
min2= df['CustomerID'].min()
med0 = df['Quantity'].median()
med1 = df['UnitPrice'].median()
med2 = df['CustomerID'].median()
print("QuantMax=", max0, "QuantMin =", min0, "\n"
      "UnitPriceMax =", max1, "UnitPriceMun =", min1, "\n"
      "CustomerIDMax = ", max2, "CustomerIDMin = ", min2)
print("QuantMed = ", med0, "\n"
      "UnitPriceMed = ", med1, "\n"
      "CustomerMed", med2) #друк макс, мін і середнє для Quantity, UnitPrice, CustomerID

df = pd.read_csv(io.StringIO(response0.text))
missing_values_count = df.isnull().sum()
print(missing_values_count)