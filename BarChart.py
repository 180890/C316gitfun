import matplotlib.pyplot as plt
import pandas as pd
  
  
data = pd.read_csv('BigmacPrice.csv')
  
df = pd.DataFrame(data)
  
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])
  
plt.bar(X, Y, color='g')
plt.title("Price of BigMac")
plt.xlabel("name")
plt.ylabel("dollar_price")
  
# Show the plot
plt.show()