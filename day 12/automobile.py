import pandas as pd
import numpy as np
df = pd.read_csv("Automobile.csv")
df['price'] = df['price'].fillna(df['price'].mean())
arr=df['price']
data=np.array(arr)
data.mean()
data.min()
data.max()
data.std()