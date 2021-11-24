import pandas
from sklearn import linear_model
import matplotlib.pyplot as plt


df = pandas.read_csv("animals.csv")

X = df[['Speed']]
y = df[['Weight']]

regr = linear_model.LinearRegression()
regr.fit(X, y)

plt.scatter(X, y)
plt.show()

