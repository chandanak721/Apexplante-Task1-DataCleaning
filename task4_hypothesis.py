import pandas as pd
from scipy import stats

df = pd.read_csv("Task3_ApexPlanet/cleaned_sales_data.csv")

tech = df[df['Category']=='technology']['Sales']
furniture = df[df['Category']=='furniture']['Sales']

t_stat, p_value = stats.ttest_ind(tech, furniture)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject Null Hypothesis")
    print("Significant difference exists")
else:
    print("Fail to Reject Null Hypothesis")
    print("No significant difference")