import pandas as pd
df = pd.read_csv(r'C:\Users\anany\OneDrive\Documents\GitHub\C316gitfun\BigmacPrice.csv')
print(df)
mean = df['local_price'].mean()
print("mean : ",mean)
std = df['local_price'].std()
print("standard deviation : ",std)
median = df['local_price'].median()
print("median : ",median)