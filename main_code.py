import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
print(missing_values_count) #скільки значень відсутні у кожній колонці

df_ = df.select_dtypes(exclude=['int64', 'float64'])
for col in df_.columns:
    print(df_[col].unique()[:5])#принт перших 5 унікальних
    print(df_[col].value_counts().head(5))#принт 5 найчастіших
    print(df_[col].value_counts().shape)


df_filtered = df[(df["Quantity"]>=0) & (df["UnitPrice"]>=0)]
print (df_filtered) #фільтрування колонок, щоб числа була більше або дорівнювали 0

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], dayfirst = True, errors = 'coerce')
print("Тип:", df['InvoiceDate'].dtype)
print("Пропущених дат:", df['InvoiceDate'].isna().sum()) #вивід кількості пропущених дат
df.info

corr_value = df['Quantity'].corr(df['UnitPrice'])
print("Кореляція між кількістю і вартістю =", corr_value) #Побудова кореляції між кількістю і вартістю
print('Кореляція між усіма числовими колонками =',  df.corr(numeric_only=True,)) #побудова кореляції між усіма стовпчиками з числовим значенням

bins = [0, 50, 70, 100, 150, 200, 250, 500, df["Quantity"].max()]
labels = ['0-50', '50-70', '70-100', '100-150', '150-200', '200-250', '250-500', '500+']
df['QuantityRange'] = pd.cut(df['Quantity'], bins=bins, labels=labels, include_lowest=True, ordered=True)
df['QuantityRange'].value_counts().reindex(labels).plot(kind='bar')
plt.title('Кількість записів у кожному діапазоні Quantity')
plt.xlabel('Діапазон Quantity')
plt.ylabel('Кількість рядків')
plt.show()