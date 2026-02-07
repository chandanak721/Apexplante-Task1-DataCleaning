import pandas as pd

df = pd.read_csv(r'C:\Users\ramup\Downloads\ApexPlanet-Internship\Task1_ApexPlanet\cleaned_sales_data.csv')




print('===== SUMMARY =====')
print(df.describe())

print('\nCategory Sales')
print(df.groupby('Category')['Sales'].sum())

print('\nRegion Profit')
print(df.groupby('Region')['Profit'].sum())
