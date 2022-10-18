import pandas as pd
df = pd.read_csv(r'C:\Users\anany\OneDrive\Documents\GitHub\C316gitfun\BigmacPrice.csv')
print(df)
mean = df['dollar_price'].mean()
print("mean of dollar_price: ",mean)
std = df['local_price'].std()
print("standard deviation of dollar_price: ",std)
median = df['local_price'].median()
print("median of dollar_price: ",median)