import pandas as pd

df = pd.read_csv("dz.csv")

print(df.groupby('City')['Salary'].mean())