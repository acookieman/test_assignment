import pandas as pd
url = "https://raw.githubusercontent.com/acookieman/test_assignment/refs/heads/main/train_data.csv"
df = pd.read_csv(url)
print (df.head())