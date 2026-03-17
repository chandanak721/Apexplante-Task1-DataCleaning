import pandas as pd

# load dataset
df = pd.read_csv("cleaned_sales_data.csv")

# create segments based on sales value
df['Segment'] = pd.cut(
    df['Sales'],
    bins=[0,1000,1700,100000],
    labels=['Low','Medium','High']
)

print("Average Profit by Segment")
print(df.groupby('Segment')['Profit'].mean())

print("\nSales by Category")
print(df.groupby('Category')['Sales'].sum())

print("\nProfit by Region")
print(df.groupby('Region')['Profit'].sum())