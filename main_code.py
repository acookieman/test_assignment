import pandas as pd
url = "https://raw.githubusercontent.com/acookieman/test_assignment/refs/heads/main/train_data.csv"
df = pd.read_csv(url)
print (df.head()) #друк "голови"
print('rows', df.shape[0] )
print ('columns', df.shape[1],)
print ("types", df.info)
