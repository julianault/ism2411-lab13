# 1. A boolean filter selects rows that meet a specific condition and leaves out rows that do not.
# 2. df["revenue"] returns a Series (one-dimensional), while df[["revenue"]] returns a DataFrame (two-dimensional). This matters when you need to work with a DataFrame instead of a single column.
# 3. Pandas makes it faster and easier to organize, filter, and analyze large amounts of data using code. It also makes the process repeatable.

# Exercise 1
import pandas as pd
df = pd.read_csv("data/retail_sales.csv")
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# Exercise 2
south = df[df['region'] == 'South']
print(len(south))
print(south.head())

# Exercise 3
print(df.sort_values('revenue', ascending=False).head(5))

# Exercise 4
big_south = df[(df['region']=='South') & (df['revenue']>1000)]
print(len(big_south))
print(big_south.head())

# Exercise 5
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print(df['per_unit'].mean())

# Exercise 6
print(df['region'].unique())
print(df['region'].value_counts())

# Exercise 7
selected = df[['region', 'product', 'revenue']]
print(selected.shape)

# Exercise 8
df.to_csv('data/explored.csv', index=False)