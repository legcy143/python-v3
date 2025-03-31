import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
from sklearn.linear_model import LinearRegression

data = "../data/lifesat.csv"
lifesat = pd.read_csv(data)

x = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

head = lifesat.head()
lifesat.plot(kind='scatter', x="GDP per capita (USD)", y='Life satisfaction')
plt.show()

model = LinearRegression()
model.fit(x, y)

print(lifesat.head())

