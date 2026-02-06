import pandas as pd

df = pd.read_csv('raw_sales_data.csv')
df = df.drop_duplicates()
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
df['Profit'] = df['Profit'].fillna(0)
df['Category'] = df['Category'].str.lower()

df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.month

Q1 = df['Profit'].quantile(0.25)
Q3 = df['Profit'].quantile(0.75)
IQR = Q3 - Q1

df = df[(df['Profit'] >= Q1-1.5*IQR) & (df['Profit'] <= Q3+1.5*IQR)]

df.to_csv('cleaned_sales_data.csv', index=False)
print('Cleaning Completed')
